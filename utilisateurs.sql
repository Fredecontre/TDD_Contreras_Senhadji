
DROP TABLE IF EXISTS Utilisateurs;
DROP TABLE IF EXISTS Liens;
DROP TABLE IF EXISTS Utilisateur_possede_lien;


--Création des tables
CREATE TABLE Utilisateurs (id INTEGER PRIMARY KEY AUTOINCREMENT, Username TEXT NOT NULL, Password TEXT NOT NULL);
CREATE TABLE Liens (id INTEGER PRIMARY KEY AUTOINCREMENT, Link TEXT NOT NULL, Id_utilisateur INTEGER, FOREIGN KEY (Id_utilisateur) REFERENCES Utilisateurs(id));

-- Création table d'associations pour associer des liens à des comptes utilisateur
CREATE TABLE Utilisateur_possede_lien (Id_utilisateur INTEGER NOT NULL, Id_lien NOT NULL, FOREIGN KEY (Id_lien) REFERENCES Utilisateurs(id),
 PRIMARY KEY (Id_utilisateur,Id_lien));


-- Création de quelques utilisateurs
INSERT INTO Utilisateurs(Username,Password) VALUES ('frede', '1M!tdePasse');
INSERT INTO Utilisateurs(Username,Password) VALUES ('user', '@S@fePassword12');
INSERT INTO Liens(Link,Id_utilisateur) VALUES ('deffunction',(SELECT id FROM Utilisateurs WHERE Username = "frede" AND Password = "1M!tdePasse"));
INSERT INTO Liens(Link,Id_utilisateur) VALUES ('deffunction2',(SELECT id FROM Utilisateurs WHERE Username = "frede" AND Password = "1M!tdePasse"));

INSERT INTO Utilisateur_possede_lien VALUES ((SELECT id FROM Utilisateurs WHERE Username = "frede" AND Password = "1M!tdePasse"),1);















