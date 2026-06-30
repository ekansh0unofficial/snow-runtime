from enum import StrEnum


class ExportFormat(StrEnum):
    """
    Specifies the file format used when exporting query results or table data.

    CSV     — comma-separated values; universal flat-file format for tabular data.
    JSON    — JavaScript Object Notation; human-readable semi-structured format.
    PARQUET — columnar binary format optimized for analytical workloads and compression.
    """
    CSV = "csv"
    JSON = "json"
    PARQUET = "parquet"
