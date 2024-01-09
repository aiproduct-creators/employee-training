# AI-Powered Employee Training Platform

AI-Powered Employee Training Platform is an innovative project that leverages chatbots to train employees. It uses Language Models to create interactive, context-aware chatbots for a variety of training scenarios.

## 🚀 Overview

This platform is designed to assist in the training and development of employees by providing a range of interactive chatbots. Each chatbot is tailored to specific training needs, making the learning process more engaging and effective.

## 🤖 Creating New Training Modules

To expand the platform's capabilities, you can easily create new training modules. Here's a quick guide:

1. **Duplicate a Module**:
   - Navigate to the `pages` folder.
   - Duplicate any `.py` file (referred to as a module) which contains the base code for a bot.

2. **Rename the Module**:
   - Rename the duplicated file to match the new training module's focus.

3. **Modify the Prompt**:
   - Open `trainer.py` and locate a suitable prompt.
   - Copy and modify this prompt according to the new module's requirements.
   - Import this new prompt into the newly created `.py` file.

That's it! Your new training bot is ready for use.

## 🖥️ Setup Guide

Setting up the AI-Powered Employee Training Platform environment requires a few steps:

1. **Clone the Repository**:

   ```shell
   git clone git@github.com:bdhaval/employee-training.git
   cd employee-training
   ```
2. **Install Dependencies**:

    Ensure you have Python installed, then run:

   ```shell
   pip install -r requirements.txt
   ```
3. **Run the Application**:

    To start the platform, run:
   ```shell
   streamlit run home.py
   ```