# Attention-Guided Hierarchical Structure Aggregation for Image Matting
This is the official implementation of HAttMatting(CVPR2020)<br/>

Code and paper is coming soon!!!<br/>

## News
0. The dataset link is : <a href="https://drive.google.com/file/d/1ljJkWONPfJzylkZg_1HaGRoaRaaiAxRu/view?usp=sharing"> Distinctions-646</a>. <br/>
1. The data set is now fully open to the public. If you use it for non-commercial uses, please send us an email to access the link if necessary.
2. The thumbnail from our dataset have been uploaded.
<table style="margin-left: auto; margin-right: auto;">
        <tr>
            <td>
                <img src="https://github.com/wukaoliu/CVPR2020-HAttMatting/blob/master/figures/train-img-example.png" width="384" height="256">
            </td>
            <td>  
                <img src="https://github.com/wukaoliu/CVPR2020-HAttMatting/blob/master/figures/train-gt-example.png" width="384" height="256">
            </td>
        </tr>
        <tr>
            <td align="center">
                    Training Image
            </td>
            <td align="center">
                    Training GT
            </td>
        </tr>
</table>
3. Our project Page is now fully open to the public, including pipelines, data set examples, etc. Paper will be open in two days.<br/>
4. The file for generating the composition dataset has been uploaded. It can synthesize data three times faster than the original code, which can save about two days of waiting!!!

### Project Page
<p>Our Project Page is available now: <a href="https://wukaoliu.github.io/HAttMatting/">HAttMatting</a>. The more contents is updating.</p>

## Visual Results
<table style="margin-left: auto; margin-right: auto;">
        <tr>
            <td>
                <!--左侧内容-->
                <img src="https://github.com/wukaoliu/CVPR2020-HAttMatting/blob/master/results/ball-img16.png" width="384" height="256">
            </td>
            <td>
                <!--右侧内容-->
                <img src="https://github.com/wukaoliu/CVPR2020-HAttMatting/blob/master/results/ball-our.png" width="384" height="256">
            </td>
        </tr>
        <tr>
            <td>
                <!--左侧内容-->
                <img src="https://github.com/wukaoliu/CVPR2020-HAttMatting/blob/master/results/retriever-img0.png" width="384" height="256">
            </td>
            <td>
                <!--右侧内容-->
                <img src="https://github.com/wukaoliu/CVPR2020-HAttMatting/blob/master/results/retriever-our-img0.png" width="384" height="256">
            </td>
        </tr>
        <tr>
            <td align="center">
                    Input Image
            </td>
            <td align="center">
                    Our Result
            </td>
        </tr>
</table>


## Dataset

Our Dinstinctions-646 are composed of 646 foreground images with manually annotated alpha mattes.  We will release this dataset for encouraging future research on trimap-free image matting. We will not post a public download link and if you need this dataset for academic research, please send us a email for getting it.



## Citation
If you use this code and dataset for your research, please cite our paper:
```
@InProceedings{Qiao_2020_CVPR,
    author = {Qiao, Yu and Liu, Yuhao and Yang, Xin and Zhou, Dongsheng and Xu, Mingliang and Zhang, Qiang and Wei, Xiaopeng},
    title = {Attention-Guided Hierarchical Structure Aggregation for Image Matting},
    booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    month = {June},
    year = {2020}
}
```

