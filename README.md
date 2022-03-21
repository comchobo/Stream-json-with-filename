# Stream-json-with-filename

This code uses ijson==3.14. Not sure availability with other dependency.

It streams json file with filename(file path). All you have to do is simply putting filename list and run.

Example:

```dataset_from_path_list([filepath1, filepath2, ... ])```

returns iterable.

if filepath1 contains [['hello'], ['my']] and filepath2 contains [['name'], ['is']],
then following code

```
iterable = dataset_from_path_list([filepath1, filepath2])
iterable.__iter__()
iterable.__next__()
iterable.__next__()
iterable.__next__()
```

will return :

```
['hello']
['my']
['name']
```
