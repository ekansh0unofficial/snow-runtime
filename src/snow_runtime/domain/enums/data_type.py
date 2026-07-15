from enum import StrEnum


class DataType(StrEnum):
    """
    Represents Snowflake SQL data types used in schema introspection and metadata.

    INTEGER   — whole number; maps to Snowflake NUMBER with zero decimal scale.
    FLOAT     — double-precision floating point number.
    DECIMAL   — fixed-precision decimal (NUMERIC); preferred for monetary values.
    VARCHAR   — variable-length Unicode string.
    BOOLEAN   — logical true/false value.
    DATE      — calendar date (year, month, day) with no time component.
    TIME      — time of day with microsecond precision and no date component.
    TIMESTAMP — combined date and time with optional timezone.
    VARIANT   — semi-structured data; can hold JSON, XML, Avro, or Parquet values.
    OBJECT    — key-value pairs; a sub-type of VARIANT for JSON object structures.
    ARRAY     — ordered list; a sub-type of VARIANT for JSON array structures.
    BINARY    — raw binary data (VARBINARY / BYTES).
    GEOGRAPHY — geospatial data in GeoJSON format using WGS84 coordinates.
    """

    INTEGER = "integer"
    FLOAT = "float"
    DECIMAL = "decimal"
    VARCHAR = "varchar"
    BOOLEAN = "boolean"
    DATE = "date"
    TIME = "time"
    TIMESTAMP = "timestamp"
    VARIANT = "variant"
    OBJECT = "object"
    ARRAY = "array"
    BINARY = "binary"
    GEOGRAPHY = "geography"
