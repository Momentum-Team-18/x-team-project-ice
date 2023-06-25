
# QuestionsAPI

QuestionsAPI is a Django REST Framework that provides endpoints that enables users to register, login, post questions and answers regarding topics of their choosing.


## API Reference

#### URL

https://questionapi.onrender.com

#### Create User

```https://questionapi.onrender.com
  POST /auth/users/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`   |`str`     |                                   |
|`username` |`str`     |                                   |
| `password`| `str`    |                                   |

#### Create User

```https://questionapi.onrender.com
  POST /auth/token/login/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`username` |`str`     |                                   |
| `password`| `str`    |                                   |

#### Create Token

```https://questionapi.onrender.com
  POST /auth/users/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`   |`str`     |                                   |
|`username` |`str`     |                                   |
| `password`| `str`    |                                   |

#### Logout

```https://questionapi.onrender.com
  POST /auth/token/logout/
```
#### Create Question

```https://questionapi.onrender.com
  POST /questions/
```

| Parameter        | Type     | Description                       |
| :--------        | :------- | :-------------------------------- |
| `question_title` |`str`     |                                   |
|`questions_text`  |`str`     |                                   |

#### List of All Questions

```https://questionapi.onrender.com
  GET /questions/
```

#### List of All Questions From a User

```https://questionapi.onrender.com
  GET /questions/user/
```
#### Create Answer

```https://questionapi.onrender.com
  POST /questions/answer/
```

| Parameter        | Type     | Description                       |
| :--------        | :------- | :-------------------------------- |
| `answer_text`    |`str`     |                                   |
|`related_question`| `int`    |                                   |

#### Return Question with Related Answers

```https://questionapi.onrender.com
  GET /questions/pk/
```