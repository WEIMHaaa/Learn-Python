from typing import Any, Union

import wget

url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'

filename: Union[Union[str, None, bytes], Any] = wget.download(url)



