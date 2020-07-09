# shell

## some common command line

`echo`: prints out its arguments

`which`: find out the file

`pwd`: print current working directort

`cd`: change directory

`ls`: list

`man`: manual page

`> file`: write into a file

`< file`: read from a file

`>>`: append to a file

`|`: lets you “chain” programs such that the output of one is the input of another

`sudo`: do something as super user

`tee`: open a file for writing

`touch`:

`int`:

## shell and scripting

```shell
foo=bar #assign the value of foo as bar
echo "$foo" #prints bar
echo '$foo' #prints $foo

mcd () {
    mkdir -p "$1" #creates a directory
    cd "$1" #cd into it
}
```

Here are some special variables:

- `$0`: Name of the script

- `$1` to `$9`: Arguments to the script. `$1` is the first argument and so on.

- `$@`: All the arguments

- `$#`: Number of the arguments

- `$?`: Return code of the previous command

- `!!`: Entire last command, including arguments. A common pattern is to execute a command only for it to fail due to missing permissions; you can quickly re-execute the command with sudo by doing `sudo !!`

- `$_`: Last argument from the last command. If you are in an interactive shell, you can also quickly get this value by typing `Esc` followed by `.`
