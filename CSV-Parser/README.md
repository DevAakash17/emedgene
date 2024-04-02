## CSV Parser/Stringifier

- Parser: Read a CSV text file and convert it to a data structure that can be later utilized by any program
- Stringifier: Convert a defined data structure to a CSV text file

### What's a CSV file?

A CSV (comma-separated values) file is a text file that has a specific format which allows data to be saved in a table structured format.
Each line in a CSV file denotes a row and a delimiter (usually comma) is used to separate cells/columns within a row.

```csv
Name,Email,Phone Number,Address
Bob Smith,bob@example.com,123-456-7890,123 Fake Street
Mike Jones,mike@example.com,098-765-4321,321 Fake Avenue
```

### Exercise

#### Parser

Write a CSV parser (in a language of your choice) that reads any CSV file and outputs a list of list. Each item of the list represents a row and within that item list, each sub-item represents the cell value.

For above example output should be something similar to:
```json
[
    ["Name","Email","Phone Number","Address"],
    ["Bob Smith","bob@example.com","123-456-7890","123 Fake Street"],
    ["Mike Jones","mike@example.com","098-765-4321","321 Fake Avenue"]
]
```

#### Stringifier

Write a CSV stringifier that takes a list of list of strings as input and outputs it as CSV text file.
Essentially the opposite of the above parser

### Rules

- Prepare test cases first (input CSV files and respective outputs) considering all the edge cases.
- Cannot use regex
- Obviously cannot use an existing CSV parser library