from __future__ import print_function
from Skeleton import MusicTheory
from Skeleton import Constants
from Arranging.Arranging import *
import InitializeSectionsHelper
import InitializeChordsAndPhraseHelper


import sys
import math
import random
import collections
class Propulsion: 

    def __init__ ( self, movement, selectedTempo ) : 
        
        self.complexity = movement['complexity'] 
        self.rhythmSpeed = movement['rhythmSpeed']
        self.selectedTempo = selectedTempo
 
        if ( 0 ) : 
            print ( "Mood: Propulsion" ) 
            print ( 'Complexity: ', self.complexity ) 

        self.percussionDesc = ['drumsKit' ] 

        self.layers = {
            'bass1': { 'density': 1, 'range': 'low', 'type': '' },
            'bass2': { 'density': 1, 'range': 'low', 'type': '' },
            'loStrings': { 'density': 1, 'range': 'low', 'type': 'strings' },
            'leftPianoBass': { 'density': 1, 'range': 'low', 'type': '' },

            'mel5' :   { 'density': 1, 'range': 'all', 'type': '' },


            'rightPiano': { 'density': 1, 'range': 'mid', 'type': '' },
            'midStrings': { 'density': 1, 'range': 'mid', 'type': 'strings' },
            'drumsKit' :  { 'density': 1, 'range': 'mid', 'type': 'percussion' },

            'arpStrings': { 'density': 1, 'range': 'midToHi', 'type': 'strings' }, 

            'hiStrings': { 'density': 1, 'range': 'hi', 'type': 'strings' },
            'drumsCymbalSwell' : { 'density': 1, 'range': 'hi', 'type': 'percussion' },
            'piano1':  { 'density': 1, 'range': 'all', 'type': '' },
            }
        


        self.MaxAndMinLayersForEnergy = { 
            'high'  : { 'max': 11, 'min': 8, 'initialMax': 8,  'initialMin': 6, 'loRangeMax': 4, 'loRangeMin': 2 }, 
            'medium': { 'max': 8,  'min': 5, 'initialMax': 6,  'initialMin': 4, 'loRangeMax': 3, 'loRangeMin': 1 }, 
            'low'   : { 'max': 4,  'min': 2, 'initialMax': 4,  'initialMin': 2, 'loRangeMax': 2, 'loRangeMin': 1 }, 
            }

        

        self.arrange = Arranging ( "Propulsion", self.layers, False ) #useDefault = False 

        # set the initial phrase length
        if ( movement['duration'] <= 45 ) : 
            self.possiblePLs = [ 2 ] 
            self.primaryPL   = random.choice(self.possiblePLs) 
        elif ( movement['duration'] > 45 and movement['duration'] <= 90 ) : 
            self.possiblePLs = [ 4 ] 
            self.primaryPL   = random.choice(self.possiblePLs) 
        else : 
            self.possiblePLs = [ 4, 4, 3, 4, 5 ] 
            self.primaryPL   = random.choice(self.possiblePLs) 
        
        self.possiblePLs = [ 4 ] 
        self.primaryPL   = random.choice(self.possiblePLs) 

            
        # set the initail BPM
        self.possibleBPMs = [ x for x in range ( 132, 140, 1) ] 
        self.primaryBPM = random.choice ( self.possibleBPMs ) 
            
        # set the initial scale
        self.possibleKeys = MusicTheory.AllKeys
        self.primaryScale = random.choice ( self.possibleKeys ) 
            
        # set the initial TSE
        if ( self.complexity == 'super_simple' ) : #95 % probability that tse remains same
            self.possibleTSEs = [ '4/4', '3/4', '4/4'  ] 
        elif ( self.complexity == 'simple' ) : #95 % probability that tse remains same
            self.possibleTSEs = [ '2/4', '3/4', '4/4'  ] 
        elif ( self.complexity == 'semi_complex' ) : #90 % probability that tse remains same            
            self.possibleTSEs = [ '3/4', '4/4', '5/4', '7/4', '3/8', '6/8', '7/8' ] 
        elif ( self.complexity == 'complex1' ) : #80 % probability that tse remains same
            self.possibleTSEs = [ '4/4', '5/8', '6/8', '9/8', '11/8', '13/8', '3/16' ]                           

        self.primaryTSE = random.choice ( self.possibleTSEs ) 

        self.minUniqCPs =  len(movement['uniqTSEs'])
        self.minUniqCPs =  1
        self.maxUniqCPs = 7
        
        if ( self.minUniqCPs > self.maxUniqCPs ) :
            self.maxUniqCPs = self.minUniqCPs

        self.uniqTSEIds = movement['uniqTSEs']


        

        
        if ( 1 ) : 
            print ( "TSE: ", self.primaryTSE ) 
            print ( "BPM: ", self.primaryBPM ) 
            print ( "KEY: ", self.primaryScale ) 
            print ( "PL : ", self.primaryPL )

            print ( "Number of UniqTSEs: ", len( movement['uniqTSEs'] ) ) 
            print ( "XXX" , self.uniqTSEIds ) 

        movement['sectionSettings'][0]['bassRhythmType'] = 'popRhythms' 
        
        if ( 0 ) :
            print ( "All Options: " ) 
            for rhy in bassRhythmOptions : 
                print ( rhy ) 
            print() 
            print ( "Chosen Options: " ) 
            for rhy in self.bassRhythm : 
                print ( rhy, self.bassRhythm[rhy] ) 
            print() 
            
                
        self.InitializeMoodForSimple ( movement['sectionSettings'] ) ;

        #if ( self.complexity.endswith('simple') ) : 
        #    self.InitializeMoodForSimple ( movement['sectionSettings'] ) ;
        #else : 
        #    print ( "In the roadmap! Abort!" ) 
        #    sys.exit(0) 


    def InitializeMoodForSimple ( self, sections ) : 
        

        moodSpecificInfo = { 'fills': True }

        self = InitializeSectionsHelper.InitializeSectionsComplex ( self, sections, moodSpecificInfo ) 

        self = InitializeChordsAndPhraseHelper.InitializeChordsAndPhraseForSections ( self, sections ) 

        #sys.exit(0)         
        if ( 1 )  : 
            print() 
            print ( "Arrangement for Movement" ) 
            for secId in self.sections : 
                print ( "Section: ", secId, "Uniq Mel Id: ", self.sections[secId]['melId'], "startingMnum: ", self.sections[secId]['startMNum'], "endMNum: ", self.sections[secId]['endMNum'], 'tse: ', self.sections[secId]['tse'] ) 
                uniqCPId = self.sections[secId]['melId'] 
                numChordsInPhrase = self.uniqCPSettings[uniqCPId]['numChords']
                phNum = 0
                for chId in self.sections[secId]['chords'] : 
                    if ( chId % numChordsInPhrase == 0 ) :
                        print ( "\tPhrase: ", phNum + 1, self.sections[secId]['phrases'][phNum] ) 
                        phNum += 1
                    print ( "\t\tChord: ", chId, self.sections[secId]['chords'][chId] ) 
                print() 

        #sys.exit(0) 




    def setPercussionSettings ( self, tse ) : 
        
        type = 'defaultDrumKit'
        middleBeats = Constants.TSEBeatInfo[tse]['middleBeats'] 
        halfBeats = Constants.TSEBeatInfo[tse]['halfBeats'] 
        strongDownBeats = Constants.TSEBeatInfo[tse]['strongDownBeats'] 
        weakDownBeats = Constants.TSEBeatInfo[tse]['weakDownBeats'] 
        numBeats = Constants.TSEs[tse]['num16thBeats'] 
        oneExtra8thBeatForBassDrumsFilled = False

        BeatInfo = collections.OrderedDict() 

        numBeats = Constants.TSEs[tse]['num16thBeats'] 
        eopStartBeat = numBeats + 1 - random.choice ( [ numBeats//2, numBeats//4 ] )  # end of phrase fill 
        eosStartBeat = numBeats + 1 - random.choice ( [ numBeats, numBeats, numBeats, numBeats//2, numBeats ] )  # end of section fill 
        numPatterns = 1

        patterns = collections.OrderedDict() 
        patterns[0] = { 'eosStartBeat': eosStartBeat, 'eopStartBeat': eopStartBeat }


        if ( 0 ) : 
            print ( "eop: ", eopStartBeat, "eos: ", eosStartBeat ) 


        maxUpBeats = 2
        numUpBeatsForKick = 0 
        numUpBeatsForSnare = 0 
        numUpBeatsForHihat = 0 


        beatArray = [ i for i in range ( 1, numBeats+1, 1 ) ]
        #print ( "Beat Array: ", beatArray ) 
        random.shuffle ( beatArray ) 
        #print ( "Beat Array: ", beatArray ) 


        #for i in range ( 1, numBeats+1, 1 ) : 
        for i in beatArray :
         
            if ( i in middleBeats ) : 
                BeatInfo[i] = { 
                    'kick' :       { 'probMax': 90, 'probMin': 80, 'velocityMax': 120, 'velocityMin': 70 }, 
                    'lowDkick' :   { 'probMax': 50, 'probMin': 40, 'velocityMax': 110, 'velocityMin': 70 }, 
                    'snare':       { 'probMax': 85, 'probMin': 75, 'velocityMax': 120, 'velocityMin': 100 }, 
                    'lowDsnare':   { 'probMax': 70, 'probMin': 60, 'velocityMax': 100, 'velocityMin': 70 }, 
                    'hihat':       { 'probMax': 90, 'probMin': 70, 'velocityMax': 110, 'velocityMin': 90 }, 
                    'lowDhihat':   { 'probMax': 20, 'probMin': 10, 'velocityMax': 80,  'velocityMin': 50 }, 
                    'bass' :   { 'probMax': 80, 'probMin': 70, 'velocityMax': 120, 'velocityMin': 70 }, 
                    }
            
            elif ( i in halfBeats ) : 
                BeatInfo[i] = { 
                    'kick' :       { 'probMax': 90, 'probMin': 80, 'velocityMax': 120, 'velocityMin': 70 }, 
                    'lowDkick' :   { 'probMax': 50, 'probMin': 40, 'velocityMax': 110, 'velocityMin': 70 }, 
                    'snare':       { 'probMax': 20, 'probMin': 10, 'velocityMax': 80,  'velocityMin': 40 }, 
                    'lowDsnare':   { 'probMax': 70, 'probMin': 60, 'velocityMax': 100, 'velocityMin': 70 }, 
                    'hihat':       { 'probMax': 90, 'probMin': 70, 'velocityMax': 110, 'velocityMin': 90 }, 
                    'lowDhihat':   { 'probMax': 20, 'probMin': 10, 'velocityMax': 80,  'velocityMin': 50 }, 
                    'bass' :       { 'probMax': 80, 'probMin': 70, 'velocityMax': 120, 'velocityMin': 70 }, 
                    }

            elif ( i in strongDownBeats ) : 
                
                BeatInfo[i] = { 
                    'kick' :   { 'probMax': 50, 'probMin': 40, 'velocityMax': 120, 'velocityMin': 70 }, 
                    'lowDkick' :   { 'probMax': 30, 'probMin': 20, 'velocityMax': 90, 'velocityMin': 70 }, 
                    'snare':   { 'probMax': 40, 'probMin': 20, 'velocityMax': 110, 'velocityMin': 80 }, 
                    'lowDsnare':   { 'probMax': 30, 'probMin': 20, 'velocityMax': 80, 'velocityMin': 50 }, 
                    'hihat':   { 'probMax': 85, 'probMin': 65, 'velocityMax': 100, 'velocityMin': 80 }, 
                    'lowDhihat':   { 'probMax': 10, 'probMin': 10, 'velocityMax': 80,  'velocityMin': 50 }, 
                    'bass' :   { 'probMax': 50, 'probMin': 30, 'velocityMax': 120, 'velocityMin': 70 }, 
                    }


            elif ( i in weakDownBeats ) : 
                
                    
                BeatInfo[i] = { 
                    'kick' :   { 'probMax': 70, 'probMin': 50, 'velocityMax': 120, 'velocityMin': 70 }, 
                    'lowDkick' :   { 'probMax': 30, 'probMin': 20, 'velocityMax': 90, 'velocityMin': 70 }, 
                    'snare':   { 'probMax': 25, 'probMin': 5,  'velocityMax': 60,  'velocityMin': 30 }, 
                    'lowDsnare':   { 'probMax': 30, 'probMin': 20, 'velocityMax': 80, 'velocityMin': 50 }, 
                    'hihat':   { 'probMax': 80, 'probMin': 60, 'velocityMax': 90,  'velocityMin': 60 }, 
                    'lowDhihat':   { 'probMax': 10, 'probMin': 10, 'velocityMax': 80,  'velocityMin': 50 }, 
                    'bass' :   { 'probMax': 50, 'probMin': 30, 'velocityMax': 120, 'velocityMin': 70 }, 
                    }
                
                                            
            else : 
                
                if ( numUpBeatsForKick < maxUpBeats and random.randint (0, 100 ) < 70 ) : 
                    probMaxKick = 70 
                    numUpBeatsForKick += 1
                else :
                    probMaxKick = 0 


                if ( numUpBeatsForSnare < maxUpBeats and random.randint (0, 100 ) < 70 ) : 
                    probMaxSnare = 70 
                    numUpBeatsForSnare += 1
                else :
                    probMaxSnare = 0 


                if ( numUpBeatsForHihat < maxUpBeats and random.randint (0, 100 ) < 70 ) : 
                    probMaxHihat = 70 
                    numUpBeatsForHihat += 1
                else :
                    probMaxHihat = 0 


                BeatInfo[i] = { 
                    'kick' :   { 'probMax': probMaxKick,  'probMin': 10, 'velocityMax': 80,  'velocityMin': 60 }, 
                    'lowDkick' :   { 'probMax': 5, 'probMin': 1, 'velocityMax': 90, 'velocityMin': 70 }, 
                    'snare':   { 'probMax': probMaxSnare, 'probMin': 0,  'velocityMax': 50,  'velocityMin': 20 }, 
                    'lowDsnare':   { 'probMax': 0, 'probMin': 0, 'velocityMax': 80, 'velocityMin': 50 }, 
                    'hihat':   { 'probMax': probMaxHihat, 'probMin': 10, 'velocityMax': 60,  'velocityMin': 40 }, 
                    'lowDhihat':   { 'probMax': 0, 'probMin': 00, 'velocityMax': 80,  'velocityMin': 50 }, 
                    'bass' :   { 'probMax': 0,            'probMin': 0,  'velocityMax': 0,   'velocityMin': 0 }, 
                    }
            
        #sys.exit(0) 
        return BeatInfo, patterns, type


