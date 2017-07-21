//
//  ViewController.swift
//  fashionFind
//
//  Created by Ahmed Al Dulaimy on 7/21/17.
//  Copyright © 2017 Ahmed Al Dulaimy. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var asd: UIWebView!
    override func viewDidLoad() {
        super.viewDidLoad()

        
        let url = URL (string: "http://169.254.31.36/")

        let requestObj = URLRequest(url: url!)
        asd.loadRequest(requestObj)
        

    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

