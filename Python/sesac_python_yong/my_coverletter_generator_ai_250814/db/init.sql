CREATE DATABASE IF NOT EXISTS coverletter;
USE coverletter;

CREATE TABLE session (
    session_id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE chat_history (
    chat_history_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT NOT NULL,
    chat_history VARCHAR(10)    ,
    FOREIGN KEY (session_id) REFERENCES session(session_id) ON DELETE CASCADE
);

CREATE TABLE corp_name (
    corp_name_id INT AUTO_INCREMENT PRIMARY KEY,
    corp_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE corp_info (
    corp_info_id INT AUTO_INCREMENT PRIMARY KEY,
    corp_name_id INT NOT NULL,
    corp_intro TEXT,
    ideal_talent TEXT,
    main_business TEXT,
    esg_activity TEXT,
    FOREIGN KEY (corp_name_id) REFERENCES corp_name(corp_name_id) ON DELETE CASCADE
);

CREATE TABLE recruit_info (
    recruit_info_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT NOT NULL,
    corp_name_id INT NOT NULL,
    recruit_info TEXT NOT NULL,
    FOREIGN KEY (session_id) REFERENCES session(session_id) ON DELETE CASCADE,
    FOREIGN KEY (corp_name_id) REFERENCES corp_name(corp_name_id) ON DELETE CASCADE
);

CREATE TABLE user_request (
    user_request_id INT AUTO_INCREMENT PRIMARY KEY,
    corp_name_id INT NOT NULL,
    recruit_info_id INT NOT NULL,
    my_request TEXT NOT NULL,
    FOREIGN KEY (corp_name_id) REFERENCES corp_name(corp_name_id) ON DELETE CASCADE,
    FOREIGN KEY (recruit_info_id) REFERENCES recruit_info(recruit_info_id) ON DELETE CASCADE
);

CREATE TABLE classified_type (
    classified_type_id INT AUTO_INCREMENT PRIMARY KEY,
    user_request_id INT NOT NULL,
    classified_type VARCHAR(50) NOT NULL,
    FOREIGN KEY (user_request_id) REFERENCES user_request(user_request_id) ON DELETE CASCADE
);

CREATE TABLE cover_letter (
    my_cover_letter_id INT AUTO_INCREMENT PRIMARY KEY,
    user_request_id INT NOT NULL,
    my_cover_letter LONGTEXT NOT NULL,
    FOREIGN KEY (user_request_id) REFERENCES user_request(user_request_id) ON DELETE CASCADE
);

CREATE TABLE revise_user_request (
    revise_user_request_id INT AUTO_INCREMENT PRIMARY KEY,
    my_cover_letter_id INT NOT NULL,
    revise_user_request TEXT NOT NULL,
    FOREIGN KEY (my_cover_letter_id) REFERENCES cover_letter(my_cover_letter_id) ON DELETE CASCADE
);

CREATE TABLE revised_cover_letter (
    revised_cover_letter_id INT AUTO_INCREMENT PRIMARY KEY,
    revise_user_request_id INT NOT NULL,
    revised_cover_letter LONGTEXT NOT NULL,
    FOREIGN KEY (revise_user_request_id) REFERENCES revise_user_request(revise_user_request_id) ON DELETE CASCADE
);
