package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
	"path/filepath"
	"sync"
)

type Celebrity struct {
	Name  string `json:"name"`
	Yomi  string `json:"yomi"`
	Image string `json:"image"`
}

var downloadDestFolder = "images"

func download(url string, filename string, w *sync.WaitGroup) {
	defer w.Done()
	res, err := http.Get(url)
	if err != nil {
		log.Printf("http.Get -> %v", err)
		return
	}
	data, err := ioutil.ReadAll(res.Body)
	if err != nil {
		log.Printf("ioutil.ReadAll -> %s", err.Error())
		return
	}
	defer res.Body.Close()
	if err = ioutil.WriteFile(downloadDestFolder+string(filepath.Separator)+filename, data, 0644); err != nil {
		log.Println("Error Saving:", filename, err)
	} else {
		log.Println("Saved:", filename)
	}
}

func main() {
	bytes, err := ioutil.ReadFile("celebrity_clean.json")
	if err != nil {
		log.Fatal(err)
	}
	var celebrities []Celebrity
	if err := json.Unmarshal(bytes, &celebrities); err != nil {
		log.Fatal(err)
	}
	var w sync.WaitGroup
	for idx, c := range celebrities {
		if idx&10 == 0 {
			w.Wait()
		}
		w.Add(1)
		go download(c.Image, c.Name+"_"+c.Yomi+".jpg", &w)
	}
	w.Wait()
}
