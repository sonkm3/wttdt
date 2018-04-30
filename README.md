# wttdt(when tweet then do task)
Read twitter stream, do tasks(defined by plugins) when tweet or other events came.

# requirement
```
httplib2==0.9.2
oauth2==1.9.0.post1
PyYAML==3.12
requests==2.11.1
```

# usage
`python wttdt -c config.yml`

# todo:
- paging support
- implement db store plugin
- plugins
  - filter chain
  - slack
  - async request
