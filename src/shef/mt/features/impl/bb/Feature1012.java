package shef.mt.features.impl.bb;

import java.util.HashSet;

import shef.mt.features.impl.Feature;
import shef.mt.features.util.Sentence;

/**
 * log probability of the target
 *
 *
 */
public class Feature1012 extends Feature {

    public Feature1012() {
        setIndex(1012);
        setDescription("log probability of the target");
        HashSet res = new HashSet<String>();
        res.add("ppl");
        setResources(res);
    }

    @Override
    public void run(Sentence source, Sentence target) {
        setValue((Float) target.getValue("logprob"));
    }
}
