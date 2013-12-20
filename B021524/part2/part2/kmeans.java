import java.io.IOException;
import java.lang.Object;
import java.lang.String;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class kmeans {

  public static class TokenizerMapper extends
      Mapper<Object, Text, Text, Text> {

    private Text str = new Text();
	private Text ket = new Text();
    public void map(Object key, Text value, Context context)
        throws IOException, InterruptedException {
		String s = value.toString();
		String abc = "abc";
		str.set(s);
		ket.set(abc);
		context.write(ket,str);
      }
    }
  

  public static class IntSumReducer extends
      Reducer<Text, Text, Text, Text> {
    private Text result = new Text();
	private Text p = new Text();
    private Text wrtmp = new Text();
	public void reduce(Text k, Iterable<Text> values,
        Context context) throws IOException, InterruptedException {
    	int n=0,m=0,i=0;
	  	int arrayA[]=new int[26];
	 	int arrayB[]=new int[26];
		
		for (Text str : values){
    		String tmp[]=str.toString().split("[, \\s]+");
    		n = tmp.length;		
			if(m==0&&tmp[0].equals("A")){
				for(i=0;i<n-1;i++)
				arrayA[i]=Integer.parseInt(tmp[i+1]);
			}
		
			else if(m==0&&tmp[0].equals("B")){
				for(i=0;i<n-1;i++)
				arrayB[i]=Integer.parseInt(tmp[i+1]);
			}	
			else if(m==1&&tmp[0].equals("A")){
				for(i=0;i<n-1;i++)
				arrayA[i]=Integer.parseInt(tmp[i+1]);
			}
		
			else if(m==1&&tmp[0].equals("B")){
				for(i=0;i<n-1;i++)
				arrayB[i]=Integer.parseInt(tmp[i+1]);
			}	
		m++;	
		}
		    	
    	n=n-1;
     	String Point = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
     	String group="",key="";


	  for(i=0;i<n;i++){
		if(arrayA[i]>arrayB[i]){
			key=Point.substring(i,i+1);
			group = "Group B";	
		}			
        else if(arrayA[i]<arrayB[i]){
			key=Point.substring(i,i+1);
			group = "Group A";	
		}
		else if(arrayA[i]==arrayB[i]){
			key=Point.substring(i,i+1);
			group = "Both Group A and B";	
		}
		result.set(group);
		p.set(key);
		context.write(p, result);
	  }
	  
    }
  }

  public static void main(String[] args) throws Exception {
    // debug using
//    String[] argv = { "input", "output-wc" };
//    args = argv;
    
    Configuration conf = new Configuration();
    Job job = new Job(conf, "kmeans");
    job.setJarByClass(kmeans.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setReducerClass(IntSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(Text.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}

