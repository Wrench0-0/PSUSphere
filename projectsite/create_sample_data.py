#!/usr/bin/env python
"""
Script to create sample data for PSUSphere
Run with: python manage.py shell < create_sample_data.py
Or: python create_sample_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectsite.settings')
django.setup()

from studentorg.models import College, Organization

# Create colleges
colleges_data = [
    'College of Engineering',
    'College of Science',
    'College of Arts and Sciences',
    'School of Business',
]

colleges = {}
for college_name in colleges_data:
    college, created = College.objects.get_or_create(college_name=college_name)
    colleges[college_name] = college
    status = '✓ Created' if created else '- Already exists'
    print(f"{status}: {college_name}")

print("\n" + "="*50)
print("Creating organizations...")
print("="*50 + "\n")

# Create organizations
organizations = [
    {
        'name': 'IEEE Student Branch',
        'college': 'College of Engineering',
        'description': 'Professional society for electrical and electronics engineers dedicated to advancing technology.'
    },
    {
        'name': 'ACM Student Chapter',
        'college': 'College of Engineering',
        'description': 'Association for Computing Machinery providing networking and professional development.'
    },
    {
        'name': 'Robotics Club',
        'college': 'College of Engineering',
        'description': 'Build and compete with autonomous robots in various national and international competitions.'
    },
    {
        'name': 'Debate Society',
        'college': 'College of Arts and Sciences',
        'description': 'Engage in academic debates and critical thinking discussions on contemporary issues.'
    },
    {
        'name': 'Environmental Club',
        'college': 'College of Science',
        'description': 'Promote environmental awareness and sustainable practices on campus and in the community.'
    },
    {
        'name': 'Entrepreneurship Club',
        'college': 'School of Business',
        'description': 'Support student entrepreneurs in developing and launching their business ventures.'
    },
]

for org_data in organizations:
    college = colleges[org_data['college']]
    org, created = Organization.objects.get_or_create(
        name=org_data['name'],
        defaults={
            'college': college,
            'description': org_data['description']
        }
    )
    status = '✓ Created' if created else '- Already exists'
    print(f"{status}: {org.name} ({org.college.college_name})")

print("\n" + "="*50)
print(f"Total Colleges: {College.objects.count()}")
print(f"Total Organizations: {Organization.objects.count()}")
print("="*50)
