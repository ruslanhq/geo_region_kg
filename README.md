# geo_regions_kg

This repository contains the source code for the Geo Region App, a simple application for managing orders. It is a test project that aims to fulfill specific technical requirements.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)

## Installation

To install and run this project, follow these steps:

1. Clone the repository: 
```sh
git clone https://github.com/ruslanhq/orders_app.git

cd orders_app
```
2. Rename *.env.example* to *.env*:
```sh
mv .env.example .env
```
3. Run command for up docker containers and start application:
```sh
$ make up
```

## Usage

After running the application (about 60 second), navigate to the specified local URL in your web browser.

API usage example:

Let's say we have the following data:

Region: id=1
District: id=2 (refers to the region with id=1)
Aiyl district: id=3 (refers to the district with id=2)

To get contours with a filter by region, make a GET request to the URL: http://0.0.0.0:1111/api/contours/?region_id=1

To get contours with a filter by district, make a GET request to the URL: http://0.0.0.0:1111/api/contours/?district_id=2

To get contours with a filter by aiyl district, make a GET request to the URL: http://0.0.0.0:1111/api/contours/?canton_id=3

To get contours with few filter make a GET request to the URL: http://0.0.0.0:1111/api/contours/?region_id=1&district_id=2

**On the login admin page, enter the following credentials:**

`Username: admin`

`Password: admin`


## Endpoints

The App provides the following endpoints:

1. **GET api/contours/**: List an existing contours.
2. **GET api/docs/**: OpenApi docs.
