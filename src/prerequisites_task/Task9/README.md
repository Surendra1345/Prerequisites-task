The program:

- Reads message records from a JSON file.
- Validates records using Pydantic.
- Skips and logs invalid records.
- Redacts 10-digit phone numbers from message content.
- Calculates total tokens.
- Calculates token cost using Decimal.
- Generates a UUID for every valid record.
- Records the processing time.
- Uses UTC timestamps.
- Reads secrets from environment variables.
- Includes automated pytest tests.