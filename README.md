# OS with Python

Welcome to the repository dedicated to learning Operating Systems (OS). This comprehensive resource is designed to cover key OS concepts, providing scripts and explanations to enhance your understanding. 

<p align="center">
  <img src="./OS_logo.png" alt="OS logo" width="30%" height="auto">
</p>

## Learning Operating Systems

The main topics include processes, files, synchronization, and communication.

### Repository Structure:

1. **Processes:**
   - Explore fundamental concepts related to processes in an operating system. Scripts and detailed explanations illustrate key principles.

2. **Files:**
   - Delve into the world of file systems and file management within an operating system. Scripts and explanations are tailored to enhance your understanding.

3. **Synchronization and Communication:**
   - Understand the crucial aspects of synchronization and communication in OS. Scripts and detailed explanations are available to help grasp synchronization mechanisms and communication protocols.

### How to Use This Repository:

- Navigate to each main topic directory to find scripts and explanations for that specific concept.
- Use the scripts as practical examples to reinforce theoretical knowledge.
- Refer to the detailed explanations for a deeper understanding of each concept.

Feel free to explore, learn, and contribute to this repository. If you have any questions or need clarification on any topic, don't hesitate to reach out. Happy learning!

## Collaborative Course Repository Guide

This repository also is used for our collaborative work and assignments for the course. This document provides a step-by-step guide on how to interact with the repository efficiently.

### Getting Started

1. **Fork the Main Repository:**
   - Fork the main repository into your GitHub account. This action creates a new repository in your account, and you'll be working from there.

2. **Sync Your Repository:**
   - If you've forked the repository earlier, it's essential to keep it up to date. Follow these steps to sync your fork with the latest version:
     - Configure the remote for your fork:
       ```bash
       git remote add upstream https://github.com/Alvaro8gb/OS_Python
       ```
     - Fetch any changes to the upstream:
       ```bash
       git fetch upstream
       ```
     - Checkout the local master branch of your fork:
       ```bash
       git checkout master
       ```
     - Merge changes from the upstream into your master branch:
       ```bash
       git merge upstream/master
       ```

### Making Changes

3. **Work on Assignments:**
   - Make any necessary changes to your repository according to the specific assignment.

4. **Commit and Push:**
   - Commit your changes to your local repository:
     ```bash
     git commit -m "Your descriptive commit message"
     ```
   - Push your changes to your online repository:
     ```bash
     git push origin master
     ```

5. **Create a Pull Request:**
   - Submit a pull request so that we can review your changes and merge them into the main repository.
   - If everything is satisfactory, your changes will be incorporated into the main repository. If not, you'll receive feedback on why.

### Note:
- The fork and sync process is typically done only once during the course, ensuring that you are working with the latest version of the main repository.
- Follow these guidelines to maintain a clean and organized collaborative environment. If you encounter any issues or have questions, feel free to reach out for assistance.
- Each student has an individual folder dedicated to their assignments, providing an exclusive space for uploading their scripts.


## Evaluation
### Standard 
The code of the exercises is going to be evalauted considering this standard:

1. Readability and Maintainability (1-5):
- Check if the code is well-commented and has clear, descriptive variable and function names.
- Assess the overall structure and organization of the code. Is it easy to follow?
- Look for code duplication and assess whether the code follows the DRY (Don't Repeat Yourself) principle.

2. Correctness (1-5):
- Review the code for logical errors and ensure it produces the expected output.
- Check if the code handles edge cases and error conditions appropriately.
- Verify that the code adheres to the specified requirements or design specifications.

### Scale 
Certainly! Here's the information converted to Markdown format:

**5: Excellent**

- Code is well-organized, highly readable, and maintainable.
- Adheres to coding standards and follows best practices.

**4: Good**

- Code is generally well-organized and readable.
- Adheres to coding standards but may have a few minor deviations.

**3: Average**

- Code is somewhat organized and readable, but improvements could be made.
- Adheres to some coding standards but may have notable deviations.

**2: Below Average**

- Code organization and readability need significant improvements.
- Deviations from coding standards are significant.

**1: Poor**

- Code organization and readability are severely lacking.
- Major deviations from coding standards.

### Mark 

$$ Mark = Readbility\_Maintainability * 0.2 +  Correctness * 0.8 $$
$$  1 <= Mark <= 5 $$