

# Recipe Generator 🍳

Welcome to the **Recipe Generator**! This project allows you to generate recipes dynamically based on the ingredients you have at home. It uses the [Spoonacular API](https://spoonacular.com/food-api) to fetch recipes in real-time as you type.

---

## Table of Contents

1. [About the Project](#about-the-project)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Contributing](#contributing)
7. [License](#license)
8. [Acknowledgements](#acknowledgements)

---

## About the Project

The **Recipe Generator** is a React-based web application that helps you find recipes based on the ingredients you have at home. It dynamically fetches recipes as you type, making it easy to discover new dishes without predefined templates.

---

## Features

- **Dynamic Recipe Generation**: Fetch recipes in real-time as you type ingredients.
- **Responsive Design**: Works seamlessly on all devices (desktop, tablet, mobile).
- **Debounced Search**: Reduces API calls by waiting for a pause in typing.
- **Recipe Details**: View detailed information about each recipe, including ingredients and instructions.

---

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- Node.js and npm (Node Package Manager)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/recipe-generator.git
   cd recipe-generator
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Set up the Spoonacular API key**:
   - Sign up at [Spoonacular API](https://spoonacular.com/food-api) to get a free API key.
   - Replace `YOUR_SPOONACULAR_API_KEY` in `src/api.js` with your actual API key.

4. **Run the app**:
   ```bash
   npm start
   ```

5. **Open the app**:
   - Open your browser and navigate to `http://localhost:3000`.

---

## Usage

1. **Enter Ingredients**:
   - Type the ingredients you have at home (e.g., "chicken, rice, tomato") in the input field.

2. **View Recipes**:
   - The app will dynamically fetch and display recipes containing the entered ingredients.

3. **Recipe Details**:
   - Click on a recipe to view its details, including ingredients and instructions.

---

## Technologies Used

- **React.js**: Frontend framework for building the user interface.
- **Axios**: HTTP client for making API requests.
- **Spoonacular API**: Provides recipe data.
- **CSS**: Styling and layout.

---

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch and submit a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- [Spoonacular API](https://spoonacular.com/food-api) for providing recipe data.
- Built with ❤️ by [Your Name](https://github.com/your-username).

---

Let me know if you need further assistance! 🚀
