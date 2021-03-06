from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import json
sc = SparkContext("local[4]", "MyApp")
ssc = StreamingContext(sc, 10)
ssc.checkpoint("file:///tmp/checkpointing")
lines = ssc.socketTextStream("localhost", 9999)
wlcnt=lines.countByWindow(30,10)
jslines = lines.flatMap(lambda x: [ j['venue'] for j in
json.loads('['+x+']') if 'venue' in j] )
lcnt=lines.count()
wlcnt.pprint()
lcnt.pprint()
c=jslines.count()
c.pprint()
jslines.pprint()
ssc.start()
ssc.awaitTermination()
