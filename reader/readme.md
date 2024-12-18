# 📖 Reader / Displayer: Animation Guide  

If you want to create animations with this **Reader / Displayer**, you'll need to memorize a few **keywords**:  

### 🗝️ Keywords
- `STARTH`
- `ENDH`
- `TIME`

---

## Syntax Guidelines  

### ⭐ `STARTH` and `ENDH`  
- You must always start with a `STARTH` and end with an `ENDH`.  
- **Important:**  
  - You **cannot** add a `STARTH` after another `STARTH`.  
  - Doing so will throw an **error**! 🚨  

---

### ⏳ `TIME`  
The `TIME` keyword is used to specify the time interval between frames.  

#### Example:  
If your animation has multiple frames spaced differently in time (e.g., 2 seconds, 4 seconds), you would write:  

```plaintext
TIME 2  
STARTH  
"FRAME1"  
ENDH  

TIME 4  ## for 4 seconds  
STARTH  
"FRAME2"  
ENDH  
