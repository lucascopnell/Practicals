
from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [ruby, python, visual_basic]
print([str(language) for language in languages])

print("\n The dynamic typed languages are: ")
dynamic_languages = [language.name for language in languages if language.is_dynamic()]
for i in dynamic_languages:
    print(i)


