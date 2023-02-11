# eHealth Corp

# CHANGES FOR SUPPLEMENTARY SEASON

- Refactored CWE - 352 and CWE - 798

- Added CVSS calculations to all CWEs

## Description

eHealth Corp is a fictitious clinic that has its services on display on its main page and allows for users to contact the clinic without being logged in. For patients, it allows for the booking of appointments, some personalization of their profiles, the viewing of their booked appointments and the downloading of test results associated with them by introducing the respective code.

## Authors

- Vicente Barros **97787**
- Daniel Ferreira **102442**
- Guilherme Antunes **103600**
- Mariana Andrade **103823**

## Vulnerability

- **CWE - 89** - Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
- **CWE - 79** - Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
- **CWE - 352** - Cross-Site Request Forgery (CSRF)
- **CWE - 488** - Exposure of Data Element to Wrong Session
- **CWE - 798** - Use of Hard-coded Credentials
- **CWE - 620** - Unverified Password Change
- **CWE - 521** - Weak Password Requirements
- **CWE - 522** - Insufficiently Protected Credentials
- **CWE - 434** - Unrestricted Upload of File with Dangerous Type

## Execute

### Docker

To run in docker you need just have to run the following command inside the version you want to run and execute

```bash
docker-compose up
```

The insecure version will be running on port 8000 and the secure version will be running on port 8080 you may cahnfe the port in the docker-compose.yml file

### Local

To run locally you must use the **run.sh** with the params -a and -p to specify the version and port you want to run the application.

Example:

```bash
./run.sh -a app -p 8080
```



### CSRF

With the unsafe version of the app running, run the following command in another terminal in the analysis directory:

```shell
python3 -m http.server --directory . <PORT> 
```

Note: the scam site will only be visible on 127.0.0.1:<PORT>.

**IMPORTANT**
When you start the application for the first time you must run the following urls to populate the database

    /generate/admin
    /generate/users
    /generate/appointments
    /generate/reports
