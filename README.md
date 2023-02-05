# • DOTS •

Make a function with **t, i, x, y**
- **t** -- time
- **i** -- number of dot
- **x** -- x coord
- **y** -- y coord

> All the dots in the 9x9 matrix will follow the same function, **but** each dot will differ in i, x, y values

Now based on the function's value...

**1. Size**
- if **fraction**, the dot's radius will be modified to that value.
- if **greater than 1**, the radius will be 1 (max)

**2. Color**
- if **negative**, **red** color
- if **positive**, **white** color

### Example
- `x*y - sin(t)*64`

<img src=https://user-images.githubusercontent.com/70792552/215462442-b5941842-987e-4ff6-b4df-4b18da9b905d.gif width=500>

- `(x-y)/24 - sin(t)`

<img src=https://user-images.githubusercontent.com/70792552/215462314-f9f35d90-cedc-4542-968c-4b2e704e328e.gif width=500>

- `sin(x/2) - sin(x-t) - y`

<img src=https://user-images.githubusercontent.com/70792552/215463784-2333a77c-7532-4463-a879-ec785ca9837a.gif width=500>

- `sin(3t-sqrt((x-7.5)**2+(y-6)**2))`

<img src=https://user-images.githubusercontent.com/70792552/215463353-82f13b66-42b0-4bc3-8eee-cb8468f7ea09.gif width=500>

## About
Made with tkinter in python. Inspired by *tixy.land* by [aemkei](https://github.com/aemkei)
