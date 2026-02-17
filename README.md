# PSUSphere
n3ck-hurt (Yodj Estares)
Wrench0-0 (Sean Caster F. Daep) 

Models

This project uses 5 main models to organize the data.

BaseModel

This is a base model used by all other models.
It automatically saves:

created_at – when the record was created

updated_at – when the record was last updated

This helps track changes in the database.

College

Stores the name of a college.

Each college can have:

Multiple programs

Multiple organizations

Program

Represents a course or program under a college.

Each program:

Has a name

Belongs to one college

Organization

Represents student organizations.

Each organization:

Has a name

Has a description

Can be linked to a college (optional)

Student

Stores student information.

Each student has:

Student ID

First name

Last name

Middle name (optional)

A program

A student belongs to one program.

OrgMember

Connects students and organizations.

This model records:

Which student joined

Which organization

The date they joined

This allows one student to join multiple organizations.

Admin

All models are registered in the Django Admin panel.
You can add, edit, and delete records directly from the admin interface.

Faker

The project uses Faker to generate sample data.
This makes it easier to test the system without manually entering data.