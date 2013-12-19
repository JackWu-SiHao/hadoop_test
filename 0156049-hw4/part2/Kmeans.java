import java.io.IOException;
import java.util.*;
        
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;
        
public class Kmeans {
        
 public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {
	private final static Text one = new Text("1");
	private final static Text ga = new Text("GroupA");
	private final static Text gb = new Text("GroupB");
    private Text word = new Text();
        
    public void map(LongWritable key, Text value, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
        String line = value.toString();
        StringTokenizer tokenizer = new StringTokenizer(line);
        while (tokenizer.hasMoreTokens()) {
            char[] tmp;
	    tmp = tokenizer.nextToken().toCharArray();
               word.set(String.valueOf(tmp[0])); 
	    if (tmp[1]=='A'){
	        output.collect(word, ga);
	    }
	    else
                 output.collect(word, gb);
	        
        }
    }
 } 
        
 public static class Reduce extends MapReduceBase implements Reducer<Text, Text, Text, Text> {

    public void reduce(Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
        int sum = 0;
        while (values.hasNext()) {
	     output.collect(key, values.next());
        }
    }
 }
        
 public static void main(String[] args) throws Exception {
    JobConf conf = new JobConf(Kmeans.class);
    conf.setJobName("kmeans");
        
    conf.setOutputKeyClass(Text.class);
    conf.setOutputValueClass(Text.class);
        
    conf.setMapperClass(Map.class);
    conf.setCombinerClass(Reduce.class);
    conf.setReducerClass(Reduce.class);
        
    conf.setInputFormat(TextInputFormat.class);
    conf.setOutputFormat(TextOutputFormat.class);
        
    FileInputFormat.setInputPaths(conf, new Path(args[0]));
    FileOutputFormat.setOutputPath(conf, new Path(args[1]));
        
    JobClient.runJob(conf);
 }
        
}
