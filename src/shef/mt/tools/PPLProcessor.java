/**
 *
 */
package shef.mt.tools;

import shef.mt.features.util.Sentence;
import java.io.*;

/**
 * Processes a file containing ngram probabilities and perplexities and sets the
 * corresponding values to the current sentence
 * 
 * This class requires the SRILM ngram output format
 *
 * @author Catalina Hallett
 * modified by Chris Hokamp
 *
 */
public class PPLProcessor extends ResourceProcessor {

    BufferedReader br;
    String[] valNames;
    String pplFile;

    public PPLProcessor(String pplFile, String[] valNames) {

        try {
        	// Chris: the br moves through the file under the guidance of FeatureExtractor (i.e. sentence-by-sentence) this is a really risky implementation!
            br = new BufferedReader(new InputStreamReader(new FileInputStream(pplFile), "utf-8"));
            
            // Chris - Val names are currently "logprob", "ppl", "ppl1"
            this.valNames = valNames;
            this.pplFile = pplFile;
        } catch (Exception e) {
            e.printStackTrace();
        }
        for (int i = 0; i < valNames.length; i++) {
        	System.out.println("PPLProcessor - value is: " + valNames[i]);
            ResourceManager.registerResource(valNames[i]);
        }
    }

    // Chris: this method actually parses the SRILM output, so the file needs to be in that format
    // Chris: valNames[] is used instead of a Map to feature names
    // using valNames allows the different logprob/perplexity features to reuse this method (logprob, poslogprob)
    public void processNextSentence(Sentence s) {
    	
        try {
        	// Chris: the br needs to be at the right place in the file(!) risky (see constructor)...
            String line = br.readLine();
            if (line == null) {
                System.out.println("line==null in " + new File(pplFile).getAbsolutePath() + " sent:" + s.getIndex() + " " + s.getText());
                return;
            }
            while (line.trim().isEmpty() || !line.endsWith("OOVs")) {
                line = br.readLine();
                //                            System.out.println(line);
            }
            line = br.readLine();
            //                            System.out.println(line);
            //ok, we found the line containing perplexities/log values
            String[] values = line.split(" ");
            //values we are interested in are at positions 3,5,7
            // these should be logprob, ppl, ppl1
//			System.out.println(line);
            if (values[3].equals("undefined")) {
                s.setValue(valNames[0], 0.0f);
            } else {
                s.setValue(valNames[0], new Float(values[3]));
            }
            if (valNames.length > 1) {
                if (values[5].equals("undefined")) {
                    s.setValue(valNames[1], 0.0f);
                } else {
                    s.setValue(valNames[1], new Float(values[5]));
                }
                if (values[7].equals("undefined")) {
                    s.setValue(valNames[2], 0.0f);
                } else {
                    s.setValue(valNames[2], new Float(values[7]));
                }
            }
        } catch (Exception e) {
            //               System.out.println(pplFile+" "+s.getText());
            e.printStackTrace();
        }
    }

    public void close() {
        try {
            br.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
