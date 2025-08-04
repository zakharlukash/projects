/* Code for Demo or SQL fabric database*/

CREATE TABLE [dbo].[comments]

(
    [uniqueID] [nvarchar](50) NOT NULL,
    [yearmonth] [int] NOT NULL,
    [timestamp] [datetime2](7) NOT NULL,
    [comment] [nvarchar](1000) NULL,
    [city] [nvarchar](50) NULL,
    [kpi] [nvarchar](50) NULL
) 