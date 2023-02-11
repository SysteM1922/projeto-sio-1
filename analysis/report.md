# eHealth Corp

#### Project 1 - SIO

---

## ![](https://cdn.discordapp.com/attachments/852109272262770710/1042518122550263848/logo-no-backgroundehealth.png)

---

## Index

1. Introduction

2. Overview

3. Vulnerabilites
- CWE - 89

- CWE - 79

- CWE - 352

- CWE - 488

- CWE - 798

- CWE - 620

- CWE - 521

- CWE - 522

- CWE - 434

---

## 1. Introduction

The present report serves as documentation for Project 1 of SIO which intends to explore the possible vulnerabiilites, their consequences and their counters in a webapp for a ficitious clinic: eHealth Corp.

---

## 2. Overview

To implement and counteract our selected vulnerabilites we used Flask: HTML with Boostrap on the frontend, data renderization with templating using Jinja2 and a SQLite database for data persistency on the backend.

---

## 3. Vulnerabilites

### CWE - 89 - Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

### CVSS

##### Severity: 4.3

##### Vector String: CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N

##### Breakdown

| Metric | Value | Justification                                                                                                                                            |
| ------ | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AV     | N     | The vulnerability is exploitable from a remote network, such as the internet, without requiring user interaction.                                        |
| AC     | L     | The attack requires low complexity, such as the availability of an easily guessable or known SQL injection payload.                                      |
| PR     | N     | No privileges are required to exploit the vulnerability.                                                                                                 |
| UI     | N     | No user interaction is required to exploit the vulnerability.                                                                                            |
| S      | U     | The vulnerability affects the security of the entire system, not just individual resources within the system.                                            |
| C      | L     | The vulnerability may allow an attacker to access or modify sensitive information, but the data is typically difficult to recover or exploited.          |
| I      | L     | The vulnerability may allow an attacker to modify data, but it is unlikely to have a significant impact on the integrity of the affected system or data. |
| A      | N     | The vulnerability does not affect the availability of the affected system or data.                                                                       |

#### Abstract

An example of SQL injection is when an attacker inserts Structured Query Language (SQL) code into a Web form input box to access resources or modify data.

An SQL query is a request for a database action to be taken.

Normally, when a user enters their name and password into the corresponding text boxes on a Web form for user authentication, those values are added to a SELECT query.

The user is given access if the values they submitted are found as expected; if they are not, access is refused.

However, except for names and passwords, most Web forms don't have any safeguards in place to prevent input.

In the absence of such security measures, a hacker may utilize the input boxes to give the database their own request, allowing them to download the entire database or engage with it in other illegal ways.

In this way, SQL injection can give an attacker unrestricted access to sensitive data, such as client information, personally identifiable information, trade secrets, intellectual property, and other sensitive data.

The ability to read, edit, and steal confidential data enables attackers to easily gain access to and take over a system.

#### Exploitation

In this case, SQL injection is possible in the password field of the login page, by entering an input that abuses the SQL quotation notation, for example ' or 1=1 -- as such:

![](https://cdn.discordapp.com/attachments/852109272262770710/1042661780205342750/injectionunsafe.gif)

#### Counteraction

Originally, the password is received and processed directly like so:

```python
result = db.session.execute("SELECT * FROM user WHERE email = '"+email+"' AND password = '"+password+"';").fetchall()
```

To correct this, the **werkzeug** library was employed to process the password through hashing. Furthermore, **SQL Alchemy** was used to make sure that the password matches that which is associated with the user. In pratical terms, this translates into a guard clause like the following:

```python
user = User.query.filter_by(email=email).first()
if not user or not check_password_hash(user.password, password):
    flash('Please check your login details and try again.')
    return redirect(url_for('auth.login'))
```

This results in the prevention of any type of SQL injection in this input field, as seen below:

![](https://cdn.discordapp.com/attachments/852109272262770710/1042673579071909909/safeinjection.gif)

### CWE - 79 - Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

CVSS

##### Severity: 7.1

##### Vector String: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:N/A:N

##### Breakdown

| Metric | Value | Justification                                                                                                                                                                                                                                              |
| ------ | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AV     | N     | The vulnerability is exploitable from a remote network, such as the internet, without requiring direct access to the target system. An attacker can leverage the vulnerability by crafting a malicious link or website that is visited by the target user. |
| AC     | L     | The attack requires low complexity, such as the availability of a known XSS payload or the presence of predictable input fields in the application.                                                                                                        |
| PR     | N     | No privileges or special knowledge are required to exploit the vulnerability.                                                                                                                                                                              |
| UI     | R     | User interaction is required to exploit the vulnerability, such as visiting a malicious website or clicking a malicious link.                                                                                                                              |
| S      | C     | The vulnerability only affects the security of individual resources, such as a single user account, rather than the entire system.                                                                                                                         |
| C      | H     | The vulnerability allows an attacker to access sensitive information or steal user data, such as session tokens or sensitive personal information. This could lead to unauthorized access to the target user's account or other sensitive information.     |
| I      | N     | The vulnerability does not allow an attacker to modify data, but it can still be used to steal sensitive information or gain unauthorized access.                                                                                                          |
| A      | N     | The vulnerability does not affect the availability of the affected system or data, but it still poses a serious security risk.                                                                                                                             |

#### Abstract

Attacks called Cross-Site Scripting (XSS) include injecting malicious scripts into reliable websites.

Attackers can deliver malicious code, typically in the form of a browser side script, to a separate end user by using a web application. The attacker can engage in a number of malicious actions after injecting the malicious script. The victim's computer may be used to send private information to the attacker, such as cookies that may contain session information.

When the victim has administrator rights to control a website, the attacker can send malicious requests on the victim's behalf, which could be extremely damaging for the website.

XSS attacks are broadly classified into two types: non-persistent (reflected) and persistent

- The most frequent type of cross-site scripting is non-persistent (reflected) XSS.
  The injected malicious script is "reflected" off the web server as a response that contains some or all of the input supplied to the server as part of the request in this type of attack.
  In such circumstances, the injected code travels to the susceptible website, "reflecting" the attack back to the victim's browser.
  Because it came from a trustworthy server, the code is then executed by the browser.

- The malicious script is stored on the victim web-server in a persistent (stored) XSS attack.
  The injected script is subsequently permanently saved on the web pages and returned to any user who accesses the script-containing web page.
  
  This is the type of XSS that we will be implementing and combating in this project.

Weakness repercussions include the exposure or theft of information saved in the user's cookies, as well as the jeopardization of secrecy by the installation of Trojan horse programs or other malicious software.

#### Exploitation

In the context of this project, and attacker can enter a script in the message field of the Appointments form and have said script execute on click of the "Show More" button on the Appointments listing page:
![](https://cdn.discordapp.com/attachments/852109272262770710/1042693306813001748/unsafe.gif)

#### Counteraction

This is avoided by escaping the script execution when the AJAX call is handled, transforming the input in a literal string.

Below the original and safe methods respectively:

```js
    $(document).ready(function () {
        let page = 1;
        $("#loadbutton").click(function () {
            page++;
            $.ajax({
                url: "/api/appointments?page=" + page,
                type: "GET",
                success: function (data) {
                    const appointments = data;
                    let html = "";
                    for (let i = 0; i < appointments.length; i++) {
                        html += "<tr>";
                        html += "<td>" + appointments[i].subject + "</td>";
                        html += "<td>" + appointments[i].description + "</td>";
                        html += "<td>" + appointments[i].date + "</td>";
                        html += "<td>" + appointments[i].time + "</td>";
                        html += "</tr>";
                    }
                    $("tbody").append(html);
                }
            });
        });
    });
```

```js
    $(document).ready(function () {#}
        var page = 1;#}
        $("#loadbutton").click(function () {#}
            page++;#}
            $.ajax({#}
                url: "/api/appointments?page=" + page,#}
                type: "GET",#}
                success: function (data) {#}
                    var appointments = data;#}
                    var selector = $("tbody");#}
                    for (var i = 0; i < appointments.length; i++) {#}
                        selector.append("<tr>");#}
                        selector.append($("<td></td>").text(appointments[i].subject));#}
                        selector.append($("<td></td>").text(appointments[i].description));#}
                        selector.append($("<td></td>").text(appointments[i].date));#}
                        selector.append($("<td></td>").text(appointments[i].time));#}
                        selector.append("</tr>");#}
                    }#}
                }#}
            });#}
        });#}
   });
```

The result is as follows, the script is input into the appointments table as literal text, as expected:

![](https://cdn.discordapp.com/attachments/852109272262770710/1042693348546334790/safexss.gif)

### CWE - 352 - Cross-Site Request Forgery

CVSS

##### Severity: 6.1

##### Vector String: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:N/I:H/A:N

##### Breakdown

| Metric | Value | Justification                                                                                                                                                                                                                                      |
| ------ | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AV     | N     | The vulnerability is exploitable from a remote network, such as the internet, without requiring direct access to the target system. An attacker can leverage the vulnerability by crafting a malicious website that is visited by the target user. |
| AC     | L     | The attack requires low complexity, such as the availability of a known CSRF payload or the ability to predict predictable input fields in the application.                                                                                        |
| PR     | N     | No privileges or special knowledge are required to exploit the vulnerability.                                                                                                                                                                      |
| UI     | R     | User interaction is required to exploit the vulnerability, such as visiting a malicious website or clicking a malicious link.                                                                                                                      |
| S      | C     | The vulnerability only affects the security of individual resources, such as a single user account, rather than the entire system.                                                                                                                 |
| C      | N     | The vulnerability does not allow an attacker to access sensitive information or steal user data.                                                                                                                                                   |
| I      | H     | The vulnerability allows an attacker to modify data, such as changing the target user's account settings or making unauthorized purchases.                                                                                                         |
| A      | N     | The vulnerability does not affect the availability of the affected system or data, but it still poses a serious security risk.                                                                                                                     |

#### Abstract

When a web server is constructed to receive a request from a client without any way for verifying that it was submitted intentionally, an attacker may be able to fool a client into sending an unintended request to the web server, which will be viewed as a genuine request.
This can be accomplished by a URL, image load, XMLHttpRequest, or other means, and can result in data exposure or inadvertent code execution.

To prevent CSRF attacks, web developers can implement measures such as using anti-CSRF tokens, rate-limiting requests, and same-site cookie policies.

#### Exploitation

For the purposes of this assignment, we chose to implement a fake, scam site, that would resemble the overall appearance of our real site, enough so that at least some more naïve users would fall for, as seen below:

![](https://media.discordapp.net/attachments/852109272262770710/1070352387778293882/image.png?width=1294&height=661)

In reality, it hides a malicious intent, implemented with the following hidden input, that is submitted when the user clicks the button:

```html
    <form hidden id="hack" target="csrf-frame" action="http://127.0.0.1:5000/appointment" method="POST"
        autocomplete="off">

        <input type="text" class="form-control" name="subject" id="subject" placeholder="Subject"
            value="Pain in the Arse" />Pain in the Arse

        <textarea name="description" class="form-control" id="message" cols="30" rows="4"
            placeholder="Message">HACKED!</textarea>

        <input type="date" class="form-control" name="date" id="date" placeholder="Date" value="2024-12-12" />

        <input type="time" class="form-control" name="time" id="time" placeholder="Time" value="14:12" />
    </form>

    <iframe hidden name="csrf-frame" id="frame" width="1000px" height="1000px"></iframe>
```

It appears to offer free checkups, but in reality, when clicked on, will make use of the user's stored cookies in order to inject a ficticious appointment in their account, as seen on the bottom of this user's appointment list:

![](https://media.discordapp.net/attachments/852109272262770710/1070352493105643530/image.png?width=1004&height=661)

Here's a dramatization of how this vulnerability could be exploited in a real world scenario, the user finds themselves on our scam site and wants their free checkup, so, logically, they click on the button in order to proceed. By doing this, when returning to the real eHealth Corp site, they are confronted with and alert injected by the attacker, alongside a new, ficticious appointment:

![](https://media.discordapp.net/attachments/852109272262770710/1070351112508547172/ezgif.com-gif-maker.gif)

#### Counteraction

**Flask-WTF** is a popular library for creating web forms in Flask and it provides built-in protection against CSRF attacks by including an anti-CSRF token in each form rendered by the library.

When a form is generated, Flask-WTF adds a hidden field with a unique token to the HTML code. This token is then sent back to the server when the form is submitted. On the server, Flask-WTF checks the token against the stored value and only processes the form if the token is valid. This way, even if an attacker is able to trick a user into submitting a form, the attack will be rejected because the attacker does not have access to the valid anti-CSRF token.

This way, attackers can't submit anything without having they themselves access to the page where the data they intend to submit is meant to be submitted in.

In terms of implementing this fix, it's as simple as importing the aforementioned library and adding a hidden input as the one seen below:

```html
<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
```

### CWE - 488 - Exposure of Data Element to Wrong Session

CVSS

##### Severity: 8.1

##### Vector String: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N

##### Breakdown

| Metric | Value | Justification                                                                                                                                                                                                                                          |
| ------ | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AV     | N     | The vulnerability is exploitable from a remote network, such as the internet, without requiring direct access to the target system. An attacker can leverage the vulnerability by exploiting a weakness in the session management mechanism.           |
| AC     | L     | The attack requires low complexity, such as exploiting a known vulnerability in the session management mechanism or guessing a session ID.                                                                                                             |
| PR     | N     | No privileges or special knowledge are required to exploit the vulnerability.                                                                                                                                                                          |
| UI     | N     | No user interaction is required to exploit the vulnerability.                                                                                                                                                                                          |
| S      | U     | The vulnerability affects the security of the entire system, potentially exposing all user data or the integrity of the system.                                                                                                                        |
| C      | H     | The vulnerability allows an attacker to access sensitive information or steal user data, such as session tokens or sensitive personal information. This could lead to unauthorized access to the target user's account or other sensitive information. |
| I      | H     | The vulnerability allows an attacker to modify data, such as changing the target user's account settings or making unauthorized purchases.                                                                                                             |
| A      | N     | The vulnerability does not affect the availability of the affected system or data, but it still poses a serious security risk.                                                                                                                         |

#### Abstract

The solution fails to adequately enforce the boundaries between the states of distinct sessions, resulting in data being provided to or used by the incorrect session.

#### Exploitation

By inserting a code for a test result that isn't theirs, a user can access and download another user's PDF test results, as such:
![](https://cdn.discordapp.com/attachments/852109272262770710/1042685208069152838/vilacabecudo.gif)

#### Counteraction

In the unsafe version of the app, the renderization is done as such:

```python
@tst.route("/test/", methods=["POST"])
def generate_link():
    code = request.form.get("code")
    report = Report.query.filter_by(code=code).first()
    if report is None:
        return "No report found"
    else:
        return "Your link has been generated. Click <a href='/test/"+str(report.patientId)+"/'>here</a> to view your report."
```

```html
{% extends "base.html" %}

{% block container %}
    <h1>Exam Result</h1>
    <p>{{ user.name }}</p>
    <p>{{ user.email }}</p>
    <p>{{ user.SSN }}</p>
    <p>{{ user.morada }}</p>
    <p>{{ user.contact }}</p>
    <p>{{ report.date }}</p>
    <p>{{ report.description }}</p>
    <p>{{ report.code }}</p>
{% endblock %}
```

By ensuring the current user is the same as the user with which the queried test results are associated with, we successfully protect the system against this attack vector:

```python
@tst.route("/test", methods=["POST"])
def generate_link():
    code = request.form.get("code")
    report = Report.query.filter_by(code=code).first()
    if report is None:
        return "No report found"
    elif report.patientId != current_user.id:
        return "You are not the owner of this report"
    else:
        return "Your link has been generated. Click <a href='/test/"+str(report.patientId)+"/'>here</a> to view your report."
```

```html
{% extends "base.html" %}

{% block container %}
{% if current_user.is_authenticated and current_user.id == user.id %}
    <h1>Exam Result</h1>
    <p>{{ user.name }}</p>
    <p>{{ user.email }}</p>
    <p>{{ user.SSN }}</p>
    <p>{{ user.morada }}</p>
    <p>{{ user.contact }}</p>
    <p>{{ report.date }}</p>
    <p>{{ report.description }}</p>
    <p>{{ report.code }}</p>
{% else %}
    Not your report 
{% endif %}
{% endblock %}
```

This results in the following behaviour:
![](https://cdn.discordapp.com/attachments/852109272262770710/1042680360372277269/safetests.gif)

### CWE - 798 - Use of Hard-coded Credentials

#### CVSS

##### Severity: 8.8

##### Vector String: CVSS:3.1/AV:A/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:N

##### Breakdown

| Metric | Value | Justification                                                                                                                                                                                        |
| ------ | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AV     | A     | The vulnerability is exploitable from the local system and does not require access to a network. An attacker can leverage the vulnerability by directly accessing the vulnerable software or device. |
| AC     | H     | The attack requires high complexity, such as reverse engineering the software or having physical access to the device.                                                                               |
| PR     | H     | High privileges or special knowledge are required to exploit the vulnerability, such as access to the source code or administrator privileges.                                                       |
| UI     | N     | No user interaction is required to exploit the vulnerability.                                                                                                                                        |
| S      | U     | The vulnerability affects the security of the entire system, potentially exposing all user data or the integrity of the system.                                                                      |
| C      | H     | The vulnerability allows an attacker to access sensitive information or steal user data, such as usernames and passwords, potentially compromising the entire system.                                |
| I      | H     | The vulnerability allows an attacker to modify data, such as changing the target user's account settings or making unauthorized purchases.                                                           |
| A      | N     | The vulnerability does not affect the availability of the affected system or data, but it still poses a serious security risk.                                                                       |

#### Abstract

Hard-coded credentials generally leave a big gap that allows an attacker to bypass the authentication that the software administrator has configured.
This vulnerability may be difficult to discover for the system administrator.
Even if it is detected, it can be impossible to repair, thus the administrator may be obliged to disable the product completely.

In this project, the inbound variation of this vulnerability will be explored: this is where a default administrator account is generated and a basic password is hard-coded into the product and connected with that account.
This hard-coded password is the same for each installation of the product, and system administrators often cannot change or disable it without manually editing the application or otherwise updating the software.
If the password is ever found or publicized (which is often on the Internet), anyone with this password can access the product.
Lastly, because all installations of the program will use the same password, even across businesses, huge assaults such as worms are possible.

In order to address this security risk, it is important to avoid using hard-coded credentials in software development. Instead, administrators should be required to create unique and secure passwords for each installation of the product, and the product should be designed to store these credentials securely. This can help to prevent unauthorized access and minimize the potential damage from a security breach. 
Additionally, regular security audits and testing can help to identify and address any hard-coded credentials that may be present in the product.

#### Exploitation

During development, several test users can be created and left, by accident, in the database tables , for example:

```
email: admin@admin.com

password: admin
```

#### Counteraction

One possible solution to this, and the one we chose to implement, is to develop a script that does a sanity check on the database that is exectuted on deploy, thereby ensuring that the product is deployed in a clean state.

Our implementation of this solution is as follows:

```python
def check_db_security(db):
    emails = ['admin', 'admin@admin.com', 'dev@healthcorp.com', 'tester@healthcorp.com', 'tester', 'tester']

    conn = db.engine.connect()
    c = conn.connection.cursor()

    for email in emails:
        print('Checking user: ' + email)
        c.execute("SELECT * FROM user WHERE email = '" + email + "';")
        result = c.fetchall()
        if result:
            print('User ' + email + ' found!')
            c.execute("DELETE FROM user WHERE email = '" + email + "';")
            conn.commit()
            print('Deleted user: ' + email)
        else:
            print('User ' + email + ' not found')
        print('=' * 50)
```

Forcing users to change their password on first use is a security measure that can help to mitigate the risk posed by hard-coded credentials in software systems. This approach works by requiring new users to create a unique and secure password immediately after their first successful login. By doing this, the hard-coded credentials are effectively nullified, as the attacker would need to know the newly created password in order to gain access to the product.

This type of password policy helps to ensure that new users start using secure passwords right away, reducing the risk of unauthorized access. In addition, forcing password changes on a regular basis can help to maintain the security of the system over time. By implementing this type of security measure, organizations can help to protect their data and systems from potential security breaches caused by hard-coded credentials.

### CWE - 620 - Unverified Password Change

#### CVSS

##### Severity: 8.1

##### Vector String: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N

##### Breakdown

| Metric | Value | Justification                                                                                                                                                                                                                             |
| ------ | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AV     | N     | The vulnerability is exploitable from a remote network, such as the internet, without requiring direct access to the target system. An attacker can leverage the vulnerability by exploiting a weakness in the password change mechanism. |
| AC     | L     | The attack requires low complexity, such as exploiting a known vulnerability in the password change mechanism or guessing a user's password reset token.                                                                                  |
| PR     | N     | No privileges or special knowledge are required to exploit the vulnerability.                                                                                                                                                             |
| UI     | N     | No user interaction is required to exploit the vulnerability.                                                                                                                                                                             |
| S      | U     | The vulnerability affects the security of the entire system, potentially exposing all user data or the integrity of the system.                                                                                                           |
| C      | H     | The vulnerability allows an attacker to access sensitive information or steal user data, such as changing the target user's password and compromising their account.                                                                      |
| I      | H     | The vulnerability allows an attacker to modify data, such as changing the target user's account settings or making unauthorized purchases.                                                                                                |
| A      | N     | The vulnerability does not affect the availability of the affected system or data, but it still poses a serious security risk.                                                                                                            |

#### Abstract

The product does not need knowledge of the original password or the usage of another type of authentication when creating a new password for a user.

An attacker might use this to change passwords for another account, acquiring the rights associated with that user.

#### Exploitation

By not asking for the user's current password when editing their profile, this allows a rogue agent who has access to the user's current session to lock them out of their account:

![](https://media.discordapp.net/attachments/1031594520061689916/1042666766658191411/image.png?width=489&height=623)

#### Counteraction

Simply adding a field that requires the user to input their current password ensures their account isn't currently compromised:

![](https://media.discordapp.net/attachments/1031594520061689916/1042666547170254868/image.png?width=489&height=623)

### CWE - 521 - Weak Password Requirements

#### CVSS

##### Severity: 7.5

##### Vector String: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N

##### Breakdown

| Metric | Value | Justification                                                                                                                                                                                                                                                        |
| ------ | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AV     | N     | The vulnerability is exploitable from a remote network, such as the internet, without requiring direct access to the target system. An attacker can leverage the vulnerability by exploiting the weak password requirements and guessing or cracking weak passwords. |
| AC     | L     | The attack requires low complexity, such as exploiting a known vulnerability in the password requirements or guessing a user's password.                                                                                                                             |
| PR     | N     | No privileges or special knowledge are required to exploit the vulnerability.                                                                                                                                                                                        |
| UI     | N     | No user interaction is required to exploit the vulnerability.                                                                                                                                                                                                        |
| S      | U     | The vulnerability affects the security of the entire system, potentially exposing all user data or the integrity of the system.                                                                                                                                      |
| C      | H     | The vulnerability allows an attacker to access sensitive information or steal user data, such as compromising the target user's account.                                                                                                                             |
| I      | H     | The vulnerability allows an attacker to modify data, such as changing the target user's account settings or making unauthorized purchases.                                                                                                                           |
| A      | N     | The vulnerability does not affect the availability of the affected system or data, but it still poses a serious security risk.                                                                                                                                       |

#### Abstract

To provide an assertion of identity for a system user, authentication systems frequently rely on a memorized secret (also known as a password).
As a result, it is critical that this password be sufficiently complex and difficult for an attacker to guess.
The particular criteria for how complicated a password must be vary according to the type of system being secured.
Choosing the right password requirements and enforcing them via implementation are important to the authentication mechanism's overall success.

#### Exploitation

The exploitation of this vulnerability simply surrounds the fact that a simple password is itself simple to crack, and therefore dangerous to be allowed.

#### Counteraction

By simply forbidding users from using weak passwords, we counteract this weakness

We do this by refusing to accept passwords that consist of simple or predictable sequences like being shorter than 8 characters in length, not having a digit, not having mixcased letters or a special symbol, using the following ``ìf`` statements:

```python
if len(new_password) < 8:
    flash('length should be at least 8')
    return redirect(url_for('profile.edit_profile'))
elif not any(char.isdigit() for char in new_password) :
    flash('Password should have at least one numeral')
    return redirect(url_for('profile.edit_profile'))
elif not any(char.isupper() for char in new_password):
    flash('Password should have at least one uppercase letter')
    return redirect(url_for('profile.edit_profile'))
elif not any(char.islower() for char in new_password):
    flash('Password should have at least one lowercase letter')
    return redirect(url_for('profile.edit_profile'))
elif not any(char in SpecialSym for char in new_password):
    flash('Password should have at least one of the  special symbols')
    return redirect(url_for('profile.edit_profile'))
else: 
    user.password = new_password
```

### CWE - 522 - Insufficiently Protected Credentials

#### CVSS

##### Severity: 7.5

##### Vector String: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N

##### Breakdown

| Metric | Value | Justification                                                                                                                                                                                                                                                                                                                        |
| ------ | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AV     | N     | The vulnerability is exploitable from a remote network, such as the internet, without requiring direct access to the target system. An attacker can leverage the vulnerability by exploiting insufficient protection of the target system's credentials, such as stealing clear-text passwords or unencrypted authentication tokens. |
| AC     | L     | The attack requires low complexity, such as exploiting a known vulnerability in the credential storage mechanism or accessing unsecured data storage.                                                                                                                                                                                |
| PR     | N     | No privileges or special knowledge are required to exploit the vulnerability.                                                                                                                                                                                                                                                        |
| UI     | N     | No user interaction is required to exploit the vulnerability.                                                                                                                                                                                                                                                                        |
| S      | U     | The vulnerability affects the security of the entire system, potentially exposing all user data or the integrity of the system.                                                                                                                                                                                                      |
| C      | H     | The vulnerability allows an attacker to access sensitive information or steal user data, such as compromising the target user's account.                                                                                                                                                                                             |
| I      | H     | The vulnerability allows an attacker to modify data, such as changing the target user's account settings or making unauthorized purchases.                                                                                                                                                                                           |
| A      | N     | The vulnerability does not affect the availability of the affected system or data, but it still poses a serious security risk.                                                                                                                                                                                                       |

#### Abstract

The site sends or saves authentication credentials, but it does so in an unsafe manner that enables for unwanted monitoring and/or extraction.

#### Exploitation

When editing the user profile, one can simply change the field in the URL corresponding to the user's ID to an ID of another user that exists, accessing, henceforth this user's profile editing page.

![](https://cdn.discordapp.com/attachments/852109272262770710/1042683221567090708/edituser.gif)

#### Counteraction

As previously referenced, the URL contains a field relative to the user's ID, this is because the current user's ID is passed as an argument in the routing system, as such:

```python
@prof.route('/edit_profile/<id>', methods=['Post'])
@login_required
def edit_profile(id): 
```

To counteract this, this page's URL has its ID field dropped and this argument is omitted, not being taken in consideration any longer, making it impossible for a given user to access any other editing page that would be able to alter third party data, like so:

```python
@prof.route('/edit_profile', methods=['POST'])
@login_required
def edit_profile():
```

### CWE-434 - Unrestricted Upload of File with Dangerous Type

#### CVSS

##### Severity: 7.5

##### Vector String: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N

##### Breakdown

| Metric | Value | Justification                                                                                                                                                                                                                                                                                    |
| ------ | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AV     | N     | The vulnerability is exploitable from a remote network, such as the internet, without requiring direct access to the target system. An attacker can leverage the vulnerability by uploading a file with a dangerous type, such as a script or executable, and executing it on the target system. |
| AC     | L     | The attack requires low complexity, such as uploading a file to an unprotected endpoint or exploiting a misconfigured file type validation mechanism.                                                                                                                                            |
| PR     | N     | No privileges or special knowledge are required to exploit the vulnerability.                                                                                                                                                                                                                    |
| UI     | N     | No user interaction is required to exploit the vulnerability.                                                                                                                                                                                                                                    |
| S      | U     | The vulnerability affects the security of the entire system, potentially exposing all user data or the integrity of the system.                                                                                                                                                                  |
| C      | H     | The vulnerability allows an attacker to execute arbitrary code, such as downloading malware or compromising the target system.                                                                                                                                                                   |
| I      | H     | The vulnerability allows an attacker to modify data, such as modifying system files or inserting malicious code.                                                                                                                                                                                 |
| A      | N     | The vulnerability does not affect the availability of the affected system or data, but it still poses a serious security risk.                                                                                                                                                                   |

#### Abstract

The software enables the upload or transfer of risky file types that can be automatically processed within the environment of the product.

#### Exploitation

When editing the user's profile the site allows for the uploading of a file, intended only to be of the PNG or JPEG file type. This condition is left to the user's good will, which means a bad actor could upload a dangerous file type that could jeopardize the normal workflow of the application.

In the following example, the user inputs a JPG type file and the system, predictably, accepts it.

![](https://cdn.discordapp.com/attachments/852109272262770710/1042642931279990905/changeppic.gif)

#### Counteraction

To counter this, we used a simple guard clause to impede an upload of any other file type that isn't PNG/JPEG:

```python
if image and not image.filename.endswith('.png') and not image.filename.endswith('.jpeg'):
    flash('Please upload a png or jpeg image.')
    return redirect(url_for('profile.edit_profile'))
```

This is the system's behaviour after this change:

![](https://cdn.discordapp.com/attachments/852109272262770710/1042657675688808530/changeppicsafe.gif)

---

## 4. Final Considerations

Besides the aforementioned attack vectors, we tried to implement and combat CWE-1336, commonly known as 'Template Injection' but this was counteracted in a previous version of Jinja2.

This project heavily contributed to our awareness of the necessity of developing apps and services with a focus on security, highlighting the risks of not doing so.

### Total CVSS Severity Score: 65
