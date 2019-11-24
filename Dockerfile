FROM python:3
ADD mail_fetcher.py /
ADD search_actions.json /
ADD actions.py /
CMD ["python", "./mail_fetcher.py"]
