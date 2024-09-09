---
marp: true
theme: uncover
size: 16:9
math: mathjax
---


<style scoped>
h1, h2{
  font-size: 50px
}
p {
    font-size: 25px
}
</style>

<style>
  :root {
    --color-background: #ddd;
    --color-background-code: #ccc;
    --color-background-paginate: rgba(128, 128, 128, 0.05);
    --color-foreground: #345;
    --color-highlight: #99c;
    --color-highlight-hover: #aaf;
    --color-highlight-heading: #99c;
    --color-header: #bbb;
    --color-header-shadow: transparent;
  }
</style>

## *Петербургский государственный университет путей сообщения Императора Александра I*

# Введение в Python

Ведет: *аспирант 2 года* **Волков Егор Алексеевич**

<br>
Санкт-Петербург 2024

---
## План работ
- **10** лабораторных работ
- **1** тестовая работа
- **Зачет**

---

## Задачи
- Познакомиться с понятием алгоритмов и структур данных
- Научиться работать с редактором VScode
- Научиться работать с интерпретатором CPython
- Научиться применять Python в обработке статистических данных

---

## Как работаем?


---
# AN-КОД
- В качестве метода проверки корректности выполняемой инструкции на **уровне ВМ**, данные инструкции подписаны AN-последовательностью. Используется AN-код со следующими параметрами:

$$
A = 1993
$$
$$
M(A, 5)=507
$$
$$
AM(A, 5) = 2^{20}-2^{16}+2^{5}+1
$$

---

При этом обеспечивается минимальное кодовое расстояние:
$$
dmin = 5
$$
При длине кодового слова:
$$
n = 20
$$
Тем самым избыточность 1993N-кода составляет:
$$
\log_{2}(A)=\log_{2}(1993) \approx 11 \text{ бит}
$$
---
Разрешенная комбинация формируется следующим образом:

$$
    n = 1
$$

$$
    A = 1993
$$

$$
    n_{c} = n \cdot A = 1993
$$

А проверяется следующим образом:
$$
    r_{c} = \frac{n_{c}}{A} = \frac{1993}{1993} = 1
$$

$$
    r_c \in C_{r} \rightarrow r_{c} \text{ is correct}
$$


---
##### Программно-аппаратная платформа для реализации безопасного вычисления
![bg left:40%](../mik32.png)

- MIK32 Амур
- MIK32 SDK

---
#### Предполагаемое готовое изделие
![w:800 h:600](../mik32brd.png)

---

![w:800 h:600](../mik32prot.png)

---
```c
#define A 1993

uint16_t encode(uint8_t byte) {
    return byte * A;
}


uint8_t decode(uint16_t encodedByte) {
    return encodedByte / A;
}

int check(uint8_t byte) {
    uint16_t encoded = encodeByte(byte);
    uint8_t decoded = decodeByte(encoded);
    return (byte == decoded);
}
```