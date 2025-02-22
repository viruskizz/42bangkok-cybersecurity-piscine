import { DataSource } from "typeorm"

const username = 'admin';
const password = 'password';
const database = 'vaccine';

const MysqlDataSource = new DataSource({
    type: "mysql",
    host: "db-mysql",
    port: 3306,
    username,
    password,
    database,
    entities: [],
})

const PostgresDataSource = new DataSource({
    type: "postgres",
    host: "db-postgres",
    port: 5432,
    username,
    password,
    database,
    entities: [],
})

// const SqliteDataSource = new DataSource({
//   type: 'sqlite',
//   database,
//   entities: [],
// })