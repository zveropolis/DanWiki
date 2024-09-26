# Шаблоны, соответствующие одному символу

| Шаблон                                                                                       | Описание                                                                                                                                                             |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.`                                                                                          | Один любой символ, кроме новой строки `\n`.                                                                                                                          |
| `\d`                                                                                         | Любая цифра                                                                                                                                                          |
| `\D`                                                                                         | Любой символ, кроме цифры                                                                                                                                            |
| `\s`                                                                                         | Любой пробельный символ (пробел, табуляция, конец строки и т.п.)                                                                                                     |
| `\S`                                                                                         | Любой непробельный символ                                                                                                                                            |
| `\w`                                                                                         | Любая буква (то, что может быть частью слова), а также цифры и `_`                                                                                                   |
| `\W`                                                                                         | Любая не-буква, не-цифра и не подчёркивание                                                                                                                          |
| `[..]`                                                                                       | Один из символов в скобках,  <br>а также любой символ из диапазона `a-b`                                                                                             |
| `[^..]`                                                                                      | Любой символ, кроме перечисленных                                                                                                                                    |
| `\d≈[0-9],`  <br>`\D≈[^0-9],`  <br>`\w≈[0-9a-zA-Z`  <br>`а-яА-ЯёЁ],`  <br>`\s≈[ \f\n\r\t\v]` | Буква “ё” не включается в общий диапазон букв!  <br>Вообще говоря, в `\d` включается всё, что в юникоде помечено как «цифра», а в `\w` — как буква. Ещё много всего! |
| `[abc-], [-1]`                                                                               | если нужен минус, его нужно указать последним или первым                                                                                                             |
| `[*[(+\\\]\t]`                                                                               | внутри скобок нужно экранировать только `]` и `\`                                                                                                                    |
| `\b`                                                                                         | Начало или конец слова (слева пусто или не-буква, справа буква и наоборот).  <br>В отличие от предыдущих соответствует позиции, а не символу                         |
| `\B`                                                                                         | Не граница слова: либо и слева, и справа буквы,  <br>либо и слева, и справа НЕ буквы                                                                                 |
| `$`                                                                                          | Конец строки                                                                                                                                                         |
| `^`                                                                                          | Начало строки                                                                                                                                                        |
| \|                                                                                           | Оператор _или_. Например, **col(o\|u)r** соответствует и американскому, и британскому вариантам написания слова color.                                               |
# Квантификаторы (указание количества повторений)

| Шаблон                                                           | Описание                                                                                                                                                                                         | Пример                  |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| `{n}`                                                            | Ровно n повторений                                                                                                                                                                               | `\d{4}`                 |
| `{m,n}`                                                          | От m до n повторений включительно                                                                                                                                                                | `\d{2,4}`               |
| `{m,}`                                                           | Не менее m повторений                                                                                                                                                                            | `\d{3,}`                |
| `{,n}`                                                           | Не более n повторений                                                                                                                                                                            | `\d{,2}`                |
| `?`                                                              | Ноль или одно вхождение, синоним `{0,1}`                                                                                                                                                         | `валы?`                 |
| `*`                                                              | Ноль или более, синоним `{0,}`                                                                                                                                                                   | `СУ\d*`                 |
| `+`                                                              | Одно или более, синоним `{1,}`                                                                                                                                                                   | `a\)+`                  |
| `*?`  <br>`+?`  <br>`??`  <br>`{m,n}?`  <br>`{,n}?`  <br>`{m,}?` | По умолчанию квантификаторы _жадные_ —  <br>захватывают максимально возможное число символов.  <br>Добавление `?` делает их _ленивыми_,  <br>они захватывают минимально возможное число символов | `\(.*\)`  <br>`\(.*?\)` |
# Регулярки в питоне

Функции для работы с регулярками живут в модуле `re`. Основные функции:

| Функция                                  | Её смысл                                                                                           |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `re.search(pattern, string)`             | Найти в строке `string` первую строчку, подходящую под шаблон `pattern`;                           |
| `re.fullmatch(pattern, string)`          | Проверить, подходит ли строка `string` под шаблон `pattern`;                                       |
| `re.split(pattern, string, maxsplit=0)`  | Аналог `str.split()`, только разделение происходит по подстрокам, подходящим под шаблон `pattern`; |
| `re.findall(pattern, string)`            | Найти в строке `string` все непересекающиеся шаблоны `pattern`;                                    |
| `re.finditer(pattern, string)`           | Итератор по всем непересекающимся шаблонам `pattern` в строке `string` (выдаются `match`-объекты); |
| `re.sub(pattern, repl, string, count=0)` | Заменить в строке `string` все непересекающиеся шаблоны `pattern` на `repl`;                       |