# test_task_BDSM_consulting

#### Vasyl Smutok

## Installation

Python3 must be already installed

```shell 
git clone https://github.com/Vasyl-Smutok/test_task_BDSM_consulting.git
cd test_task_BDSM_consulting
python3 -m venv venv
source venv/bin/activate  # on macOS
venv\Scripts\activate  # on Windows 
pip install -r requirements.txt  
```

#### This task was solved in two ways and I suggest you check how each of them works

* First way (Beautiful soup & Requests)
  * ```python bs4_requests/parse.py ```
* Second way (Scrapy)
  * ```python test_task/result.py```

 **Hints:** default the page will be parsed:  https://rezka.ag/series/comedy/2040-kremnievaya-dolina-2014.html,  
            but you can easily change this by creating a variable in the virtual environment ```URL_TO_PARSE```

