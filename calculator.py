import streamlit as st

# Title of the application
st.title('Simple Calculator')

# Function to perform arithmetic operations
def calculate(num1, num2, operation):
    if operation == 'Addition':
        result = num1 + num2
    elif operation == 'Subtraction':
        result = num1 - num2
    elif operation == 'Multiplication':
        result = num1 * num2
    elif operation == 'Division':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Cannot divide by zero'
    else:
        result = ''
    return result

# Sidebar menu for selecting operation
operation = st.sidebar.selectbox(
    'Select operation:',
    ('Addition', 'Subtraction', 'Multiplication', 'Division')
)

# Input fields for user to enter numbers
num1 = st.number_input('Enter first number:')
num2 = st.number_input('Enter second number:')

# Button to perform calculation
if st.button('Calculate'):
    if operation and num1 and num2:
        result = calculate(num1, num2, operation)
        st.success(f'Result: {result}')
    else:
        st.warning('Please enter valid numbers and select an operation.')

