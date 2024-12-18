# Animation Syntax Guide 🎥

To create animations with this Reader/Displayer, you need to memorize some keywords. These are:

- **STARTH** 🟢
- **ENDH** 🔴
- **TIME** ⏱️

## STARTH and ENDH Syntax

The syntax for **STARTH** and **ENDH** is straightforward:

- You must always pair **STARTH** with **ENDH**. ✅
- You cannot have a **STARTH** directly following another **STARTH**; doing so will result in an error. ⚠️

## TIME Syntax Explained

The **TIME** keyword is used to specify the duration of frames in an animation. Here's how to use it:

If your animation contains multiple frames that are spaced differently in time (e.g., 2 seconds, 4 seconds), use the following format:

```plaintext
TIME 2
STARTH
"FRAME1"
ENDH

TIME 4
STARTH
"FRAME2"
ENDH
```

This is valid syntax. ✅

## Expanding Keywords

If you want to expand the available keywords, you can do so in the `main.py` function. 🛠️

