# -*- coding: utf-8 -*-
import re
import sys
from llamafactory.cli import main

if __name__ == '__main__':
    # sys.argv = [
    #     'llamafactory-cli',
    #     'train', 
    #     'examples/train_lora/qwen2_5_lora_sft_diag_grounding.yaml', 
    # ]
    # sys.argv = [
    #     'llamafactory-cli',
    #     'chat', 
    #     'examples/inference/qwen2_5_lora_sft_diag_grounding.yaml', 
    # ]
    # sys.argv = [
    #     'llamafactory-cli',
    #     'export', 
    #     'examples/merge_lora/qwen_2_5_lora_sft.yaml', 
    # ]
    # sys.argv = [
    #     'llamafactory-cli',
    #     'chat', 
    #     'examples/merge_lora/qwen_2_5_lora_sft.yaml', 
    # ]
    # sys.argv = [
    #     'llamafactory-cli',
    #     'api', 
    #     'examples/merge_lora/qwen_2_5_lora_sft.yaml', 
    # ]
    # sys.argv = [
    #     'llamafactory-cli',
    #     'chat', 
    #     'examples/inference/qwen2_5_merged_diag_grounding.yaml', 
    # ]
    # sys.argv = [
    #     'llamafactory-cli',
    #     'api', 
    #     'examples/inference/qwen2_5_merged_diag_grounding.yaml', 
    # ]
    # sys.argv = [
    #     'llamafactory-cli',
    #     'train', 
    #     'examples/train_lora/qwen2_5_lora_sft.yaml', 
    # ]
    # sys.argv = [
    #     'llamafactory-cli',
    #     'chat', 
    #     'examples/inference/qwen2_5_lora_sft.yaml', 
    # ]
    # sys.argv = [
    #     'llamafactory-cli',
    #     'train', 
    #     'examples/train_lora/qwen2_5_lora_sft_instruct.yaml', 
    # ]
    # sys.argv = [
    #     'llamafactory-cli',
    #     'chat', 
    #     'examples/inference/qwen2_5_lora_sft_instruct.yaml', 
    # ]
    sys.argv = [
        'llamafactory-cli',
        'train', 
        'examples/train_lora/qwen2_5_lora_sft_diag_grounding.yaml', 
    ]
    sys.argv = [
        'llamafactory-cli',
        'chat', 
        'examples/inference/qwen2_5_lora_sft_diag_grounding.yaml', 
    ]
    sys.argv = [
        'llamafactory-cli',
        'export', 
        'examples/merge_lora/qwen2_5_lora_sft_diag_grounding.yaml', 
    ]
    sys.argv = [
        'llamafactory-cli',
        'chat', 
        'examples/inference/qwen2_5_merged_diag_grounding.yaml', 
    ]
    sys.argv = [
        'llamafactory-cli',
        'api', 
        'examples/inference/qwen2_5_merged_diag_grounding.yaml', 
    ]
    
    main()