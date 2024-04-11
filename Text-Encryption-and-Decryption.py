class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        # Remove spaces from the message
        message = message.replace(" ", "")
        # Calculate the number of columns based on the key
        num_columns = len(self.key)
        # Calculate the number of rows needed to fit the message
        num_rows = -(-len(message) // num_columns)
        # Add padding to the message if needed
        message += '*' * (num_columns * num_rows - len(message))
        # Create an empty matrix to store the message
        matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
        # Fill the matrix with the message characters
        for i, char in enumerate(message):
            row = i // num_columns
            col = i % num_columns
            matrix[row][col] = char
        # Encrypt the message by reading it in column-major order
        ciphertext = ''
        for col in range(num_columns):
            for row in range(num_rows):
                ciphertext += matrix[row][self.key.index(col + 1)]
        return ciphertext

    def decrypt(self, ciphertext):
        # Calculate the number of columns based on the key
        num_columns = len(self.key)
        # Calculate the number of rows needed to fit the message
        num_rows = len(ciphertext) // num_columns
        # Create an empty matrix to store the message
        matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
        # Fill the matrix with the ciphertext characters in column-major order
        idx = 0
        for col in range(num_columns):
            for row in range(num_rows):
                matrix[row][self.key.index(col + 1)] = ciphertext[idx]
                idx += 1
        # Extract the plaintext from the matrix
        plaintext = ''
        for row in range(num_rows):
            for col in range(num_columns):
                plaintext += matrix[row][col]
        # Remove padding and return the plaintext
        plaintext = plaintext.rstrip('*')
        return plaintext

# Example usage:
key = [2, 1, 3]  # Example key
cipher = TranspositionCipher(key)
plaintext = "My name is Irshad "
encrypted_message = cipher.encrypt(plaintext)
print("Encrypted message:", encrypted_message)

# Decrypting the encrypted message
decrypted_message = cipher.decrypt(encrypted_message)
print("Decrypted message:", decrypted_message)
