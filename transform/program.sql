CREATE TABLE IF NOT EXISTS ANALYTICS_PROGRAM AS

(SELECT
    gta as id,
    name as name,
    etab_uai as etab_uai
FROM
    RAW_ONISEP_PROGRAMS
) UNION

SELECT
    gta as id,
    code_uai as etab_uai,
    name as name
FROM
    RAW_PARCOURSUP_PROGRAMS
