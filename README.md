# Random Password Generator

This simple Python script generates a random password of a specified length using the `secrets` module. It includes a variety of characters, such as letters (both uppercase and lowercase), digits, and punctuation.

## Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. Clone the repository or download the script.

   ```bash
   git clone https://github.com/yourusername/random-password-generator.git
   ```

2. Navigate to the directory where the script is located.

   ```bash
   cd random-password-generator
   ```

3. Run the script.

   ```bash
   python password_generator.py
   ```

4. Enter the desired length for your password when prompted.

   ```bash
   How many characters your password will be? 12
   ```

5. The script will generate a random password and display it on the screen.

   ```bash
   Generated Password: q#7Fg$p2L!xZ
   ```

6. You can run the script multiple times with different lengths to generate passwords of varying lengths.

## Customization

Feel free to customize the script according to your needs. You can modify the character sets used in the password generation by editing the following line:

```python
password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation)) for i in range(x))
```

For example, if you want to exclude punctuation characters, you can modify it as follows:

```python
password = ''.join((secrets.choice(string.ascii_letters + string.digits)) for i in range(x))
```

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
