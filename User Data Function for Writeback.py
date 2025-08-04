import fabric.functions as fn
from datetime import datetime
import uuid

udf = fn.UserDataFunctions()

# 🔹 Function 1: Insert a new comment
@udf.connection(argName="sqlDB", alias="demodb")
@udf.function()
def comment_submission(
    sqlDB: fn.FabricSqlConnection,
    comment: str,
    yearmonth: int,
    city: str,
    kpi: str
) -> str:
    if len(comment) > 1000:
        return "Error: Comment exceeds the 1000-character limit."

    uniqueID = str(uuid.uuid4())
    timestamp = datetime.now()

    connection = sqlDB.connect()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO [dbo].[comments] 
        (uniqueID, comment, yearmonth, timestamp, city, kpi)
        VALUES (?, ?, ?, ?, ?, ?);
    """
    cursor.execute(insert_query, uniqueID, comment, yearmonth, timestamp, city, kpi)

    connection.commit()
    cursor.close()
    connection.close()

    return f"Comment submitted ✅"

# 🔹 Function 2: Edit existing comment by UUID
@udf.connection(argName="sqlDB", alias="demodb")
@udf.function()
def edit_comment_by_id(
    sqlDB: fn.FabricSqlConnection,
    uniqueID: str,
    newComment: str
) -> str:
    if len(newComment) > 1000:
        return "Error: Comment exceeds the 1000-character limit."

    connection = sqlDB.connect()
    cursor = connection.cursor()

    update_query = """
        UPDATE [dbo].[comments]
        SET comment = ?
        WHERE uniqueID = ?;
    """
    cursor.execute(update_query, newComment, uniqueID)

    rows_affected = cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()

    if rows_affected == 0:
        return f"Comment not found ⚠️ Refresh the page and try again"
    else:
        return f"Comment updated ✨"
