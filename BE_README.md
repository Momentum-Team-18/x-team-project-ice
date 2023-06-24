 Method | URL               | Input      | Output                              | Notes                                              |
| ------ | ----------------- | ---------- | ----------------------------------- | -------------------------------------------------- |
| POST    | /auth/users/| {"email": "", "username": "useruno", "password": "unoisthepass"}| create user
|POST |/auth/token/login/| {"username": "useruno", "password": "unoisthepass"} | create token|
|POST| /auth/token/logout/| | |
|POST| /questions/|{"question_title": "User Dos is the Most?", "question_text": "May dos is dos","question_author": 4}| create question|  {"id": 3, "question_title": "User Dos is the Most?", "question_text": "May dos is dos" "question_author": 4}|
|GET| /questions/ |  | List of All Questions|||
|GET| /questions/user/ |
|POST| questions/answer/| {"answer_text": "This is what I think", "answer_author": 2, "related_question": 2}|Create Answer|{"id": 1, "answer_text": "This is what I think", "answer_author": 2, "answer_date": "2023-06-23T21:16:03.624238Z", "related_question": 2, "answer_accepted": false}|

