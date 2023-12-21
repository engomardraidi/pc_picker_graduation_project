<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/engomardraidi/test_readme">
    <img src="logo.png" alt="Logo" width="130" height="130">
  </a>

  <h3 align="center">PC Picker - Backend</h3>

  <!-- <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p> -->
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#accounts">Accounts</a></li>
      </ul>
    </li>
    <!-- <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Welcome to PC Picker, your personalized guide to finding the perfect computing device tailored to your needs! Whether you're a professional in the creative industry, a student on a tight budget, or a gaming enthusiast looking for the latest and greatest hardware, PC Picker is here to simplify your decision-making process.

How it work:

The PC Picker system is an innovative solution designed to assist users in selecting the most suitable computing devices based on their budget and specific needs. This intelligent system leverages both expert systems and neural networks to provide personalized recommendations for PCs, laptops, and mobile devices.

Why you should use it:
* Receive personalized device suggestions based on your budget and field of use, ensuring a perfect match for your specific needs.
* Streamline the device selection process and save time with a user-friendly interface, eliminating the need for extensive research.
* Benefit from an evolving system that learns from your interactions, providing transparent insights into the decision-making process and ensuring up-to-date recommendations
<!-- :smile: -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Below you will find instructions on setting up project locally. To get a local copy up and running, follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python -v 3.10.13
* django
  ```sh
  pip install django
  ```
* django rest-framework
  ```sh
  pip install djangorestframework
  pip install markdown       # Markdown support for the browsable API.
  pip install django-filter  # Filtering support
  ```

### Installation

Below you will find instructions to run project.

1. Clone the repo
   ```sh
   git clone https://github.com/engomardraidi/pc_picker_graduation_project.git
   ```
2. Open proejct on your IDE then
   ```sh
   python3 manage.py super_admin # Create super admin in database
   ```
3. Run server
   ```sh
   python3 manage.py runserver
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Below you will find instructions and everything you need to use the APIs.

* Server run on
  ```sh
  http://127.0.0.1:8000/
  ```
### Accounts

1. Login
   * POST method
   * path
     ```sh
     accounts/login/
     ```
   * Body
     ```sh
     {
       "username": string,
       "password": string,
     }
     ```
   * Content-Type
     ```sh
     multipart/form-data # not allowed application/json
     ```
   * Response
     ```sh
     {
      "id": int,
      "username": string,
      "refresh_token": string,
      "access_token": string,
     }
2. Add new admin
   * Permissions: Only super admins are allowed
   * POST method
   * path
     ```sh
     accounts/new/
     ```
   * Body
     ```sh
     {
       "username": string,
       "first_name": string,
       "last_name": string,
       "email": string,
       "password": string,
     }
    * Headers
      ```sh
      Authorization: Bearer {access_token}
      ```
    * Response
      ```sh
      {
        "username": string,
        "first_name": string,
        "last_name": string,
        "email": string,
        "password": string,
        "data_joind": string,
      }

<p align="right">(<a href="#readme-top">back to top</a>)</p>
