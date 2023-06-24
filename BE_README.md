 Method | URL               | Input      | Output                              | Notes                                              |
| ------ | ----------------- | ---------- | ----------------------------------- | -------------------------------------------------- |
| POST    | /auth/users/| {"email": "", "username": "useruno", "password": "unoisthepass"}| create user
|POST |/auth/token/login/| {"username": "useruno", "password": "unoisthepass"} | create token|
|POST| /auth/token/logout/| | |
|POST| /questions/|{"question_title": "User Dos is the Most?", "question_text": "May dos is dos","question_author": 4}| create question|  {"id": 3, "question_title": "User Dos is the Most?", "question_text": "May dos is dos" "question_author": 4}|
|GET| /questions/ |  | List of All Questions|||
|GET| /questions/user/| | List of all the Users Questions|
|POST| questions/answer/| {"answer_text": "This is what I think", "answer_author": 2, "related_question": 2}|Create Answer|{"id": 1, "answer_text": "This is what I think", "answer_author": 2, "answer_date": "2023-06-23T21:16:03.624238Z", "related_question": 2, "answer_accepted": false}|
|GET| questions/pk/ ||Returns Question with All related answers|{"id": 1, "question_title": "What is the question?", "question_text": "The bird id the word", "question_author": 1, "question_is_answered": false, "answers": [{"id": 2, "answer_text": "We all live and learn", "answer_author": 2, "answer_date": "2023-06-24T14:13:53.173453Z", "related_question": 1, "answer_accepted": false}]}|