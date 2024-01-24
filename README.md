# VPN Service

Welcome to the VPN Service! Best solution for you!

___


## Features
* Individualized Dashboards: After registering on the website, users gain access to personalized dashboards designed for efficient information management.
* Information Customization: Users have the flexibility to modify their personal data directly within the dashboard, tailoring their user experience.
* Monitoring Data Usage: Users can monitor the volume of data transmitted to and from each site while utilizing the VPN.
* Insights Section: The dashboard features an insights section presenting detailed statistics on page visits, categorized based on the sites accessed through the VPN.
* Secured Site Entry: After creating a site, users can securely access it by clicking "Go to Site," which redirects through an internal proxy.
* Dynamic Routing: The routing structure appears as localhost/{domain_name}/{routes_on_original_site} for a dynamic and personalized experience.
* Link Attribute Substitution: The content of returned pages dynamically replaces link attributes, ensuring smooth and uninterrupted navigation.
* Site Creation: Clients can create multiple sites, each characterized by a structure encompassing URLs and distinctive names.
* User Registration: Individuals are welcome to sign up on the platform, establishing their user accounts.
___

## Prerequisites
Following prerequisites need to be installed on your system:

- **Docker:** You can download and install Docker from the official website: https://www.docker.com/.

## How to use

### Installing using GitHub

1. Clone the repository:
```bash
git clone https://github.com/Daniil-Pankieiev/vpn_service_test_task.git
```
2. Navigate to the project directory:
```bash
cd vpn_service_test_task
```
3. Switch to the develop branch:
```bash
git checkout develop
```
4. Create a virtual environment:
```bash
python -m venv venv
```
5. Activate the virtual environment:

On macOS and Linux:
```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```
6. Install project dependencies:
```bash
pip install -r requirements.txt
```
7. Copy .env.sample to .env and populate it with all required data.
<details>
<summary>Parameters for .env file:</summary>

- **POSTGRES_DB**: `Name of your DB`
- **POSTGRES_USER**: `Name of your user for DB`
- **POSTGRES_PASSWORD**: `Your password in DB`
- **POSTGRES_HOST** `Host of your DB`
</details>

#### Working with SQLite
1. Run database migrations:
```bash
python manage.py migrate
```
2. Start the development server:
```bash
python manage.py runserver
```

#### Working with Docker and PostgreSQL
Docker should be installed.

1. Use Docker Compose to build the Docker container:
```bash
docker-compose build
```

2. Run container:
```bash
docker-compose up
```
3. Optional: If you want to create super user:
```bash
docker ps
```
```bash
docker exec -it container_id bash
```

```bash
python manage.py createsuperuser
```


## Navigation

 - Access the Service at http://127.0.0.1:8000/accounts/register/


## Contributing
Feel free to contribute to these enhancements, and let's make our Airport Service API even better!
## Conclusion

Thank you for using the VPN Service! 
