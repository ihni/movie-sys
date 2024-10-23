class Seat:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.is_available = True
        self.name = self.generate_name()
    
    def generate_name(self):
        row_letter =  ""
        row_index = self.row

        while row_index >= 0:
            row_letter = chr(row_index % 26 + ord('A')) + row_letter
            row_index = row_index // 26 - 1  # Move to the next "digit"

        column_number = self.column + 1  # Convert column index to 1-based
        return f"{row_letter}{column_number}"
    
    def __str__(self):
        return f"{self.is_available} ({self.name})"