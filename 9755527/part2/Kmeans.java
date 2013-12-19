import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;


public class Kmeans {

  public static class TokenizerMapper extends
      Mapper<Object, Text, Text, Text> {
	
	
    private Text one;
    private Text word = new Text();
	private int i=0;
	String group="";
    public void map(Object key, Text value, Context context)
        throws IOException, InterruptedException {
      StringTokenizer itr = new StringTokenizer(value.toString(),",");
	  
      while (itr.hasMoreTokens()) {			
			i=0;
			StringTokenizer itr2 = new StringTokenizer(itr.nextToken());
				group=itr2.nextToken();
			    while (itr2.hasMoreTokens()) {
					
					i++;
					word.set(""+(char)(i+64));				
					one=new Text("Group"+group+"           "+itr2.nextToken());
					context.write(word, one);
					}
      }
    }
  }
  

  

  public static class IntSumReducer extends
      Reducer<Text, Text, Text, Text> {
    private Text result;

    public void reduce(Text key, Iterable<Text> values,
        Context context) throws IOException, InterruptedException {
      int smallest = 1000000;	  
	  int temp=0;
	  String temp2="";	  
	  String group="";
      for (Text val : values) {

		String[] names = val.toString().split("           ");
		temp2=names[0];
	  if(names.length>1)
	  {		
		temp=Integer.valueOf(names[1]);
		}

        if(smallest>=temp){
			smallest = temp;
			group=temp2;
			}
		
			
      }
      result= new Text(group);
      context.write(key, result);
    }
  }

  public static void main(String[] args) throws Exception {
    // debug using
//    String[] argv = { "input", "output-wc" };
//    args = argv;
    
    Configuration conf = new Configuration();
    Job job = new Job(conf, "K means");
    job.setJarByClass(Kmeans.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(IntSumReducer.class);
    job.setReducerClass(IntSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(Text.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}

