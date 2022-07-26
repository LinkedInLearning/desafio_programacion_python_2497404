import re


def slugify(texto):

    slug = (texto
        .lower()
        .strip()
        .replace(" ", "-")
    )

    slug = re.sub("[^\w\-]", "", slug)
    return slug


print(slugify("texto% con caracteres$# especial-es")) # texto-con-caracteres-especial-es
print(slugify("Este es un ejemplo!!!")) # este-es-un-ejemplo
