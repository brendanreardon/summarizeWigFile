workflow summarizeSomaticCoverage {
    String pairId
    File coverageFile

    call summarizeWigFile {
        input: pairId=pairId,
            wigFile=coverageFile
    }

    output {
        summarizeWigFile.somatic_mutation_covered_bases_capture_file
    }
}

task summarizeWigFile {
    String pairId
    File wigFile

    command {
        python /home/summarizeWigFile --pairId ${pairId} --wigFile ${wigFile}
    }

    output {
        File somatic_mutation_covered_bases_capture_file="${pairId}.somatic_coverage_summary.txt"
        # Int
    }

    runtime {
        docker: "breardon/summarizeWigFile:1.0"
        memory: "1 GB"
        cpu: "1"
        disks: "local-disk 2 HDD"
    }
}
