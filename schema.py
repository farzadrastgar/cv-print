from pydantic import BaseModel, Field
from typing import List, Optional


# ---------------------------
# Personal Info
# ---------------------------
class PersonalInfo(BaseModel):
    name: str
    title: str
    email: str
    location: str
    relocation: bool
    linkedin: str
    gitlab: str


# ---------------------------
# Education
# ---------------------------
class EducationItem(BaseModel):
    degree: str
    institution: str
    location: str
    start: str
    end: str


# ---------------------------
# Experience
# ---------------------------
class ExperienceItem(BaseModel):
    title: str
    company: str
    start: str
    end: str
    place: Optional[str] = None
    bullets: List[str]


# ---------------------------
# Skills
# ---------------------------
class Skills(BaseModel):
    programming_languages: List[str]
    web: List[str]
    frameworks: List[str]
    databases: List[str]
    architecture: List[str]
    devops: List[str]


# ---------------------------
# Languages
# ---------------------------
class LanguageItem(BaseModel):
    language: str
    level: str


# ---------------------------
# Certificates
# ---------------------------
class CertificateItem(BaseModel):
    name: str
    issuer: str
    year: str


# ---------------------------
# Main CV Schema
# ---------------------------
class CVSchema(BaseModel):
    date: str

    personal_info: PersonalInfo

    profile: str

    education: List[EducationItem]

    experience: List[ExperienceItem]

    skills: Skills

    languages: List[LanguageItem]

    certificates: List[CertificateItem]

    soft_skills: List[str]

    interests: List[str]