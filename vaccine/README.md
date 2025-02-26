# Vaccine

## Prepare
To prepare test environment with DVWA. it will create resources follow
- MYSQL
- Posgresql
- SQLite
- DVWA
- Docker network named as `dvwa_web`

```sh
make dvwa
```

To Install an Vaccine App, It will create 
- python app
- Network connectivity with `dvwa_web`

```sh
make app
```

## How to use
Command line option
```
./vaccine <url> -o [output] -X [method] -H [header]
```

Example
```
./vaccine http://web:8000/pgsql -H User-Agent=vaccine-client -H Connection=keep-alive
```

### Options


## Ref
- [Posgresql]

[Posgresql]: https://neon.tech/postgresql/postgresql-administration/postgresql-describe-table
https://www.invicti.com/blog/web-security/sql-injection-cheat-sheet/
https://github.com/OWASP/www-project-web-security-testing-guide/blob/master/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection.md

https://github.com/payloadbox/sql-injection-payload-list